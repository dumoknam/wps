from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, generics

from items.models import Item
from items.serializers import ItemsListSerializer
from members.permission import IsUser
from .models import Basket, Bill
from .serializers import BasketSerializer, OrderSerializer
from members.serializers import UserSerializer

User = get_user_model()


class ListCreateBasketItemView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        user = request.user
        baskets = Basket.objects.filter(user=user, order_yn=False)
        serializer = BasketSerializer(baskets, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        try:
            item = Item.objects.get(pk=request.data.get('item_pk'))
        except Item.DoesNotExist:
            data = {'error': '존재하지 않는 item입니다'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if Basket.objects.filter(user=user, item=item, order_yn=False).exists():
            data = {
                'error': '이미 장바구니에 있는 item입니다. patch를 이용해주세요'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        Basket.objects.create(user=user, item=item, amount=request.data.get('amount'))
        baskets = Basket.objects.filter(user=user, order_yn=False)
        serializer = BasketSerializer(baskets, many=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):
        user = request.user
        try:
            cart_item = Basket.objects.get(pk=request.data.get('cart_item_pk'), user=user, order_yn=False)
        except Basket.DoesNotExist:
            data = {'error': '존재하지 않는 장바구니 속성입니다'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        add_amount = request.data.get('add_amount')
        amount = request.data.get('amount')

        if add_amount:
            add_amount = int(add_amount)
        if amount:
            amount = int(amount)

        # 예외사항 check
        if add_amount and amount:
            data = {'error': 'add_amount, amount 모두 있습니다'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        if not add_amount and not amount:
            data = {'error': 'add_amount, amount 모두 없습니다'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        if cart_item.amount == amount or add_amount == 0:
            data = {'error': 'amount에 변화가 없습니다'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if add_amount:
            if cart_item.amount + add_amount <= 0:
                data = {'error': 'amount가 0 또는 음수입니다'}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            cart_item.amount += add_amount

        if amount:
            if amount <= 0:
                data = {'error': 'amount가 0 또는 음수입니다'}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            cart_item.amount = amount

        cart_item.save()
        return self.get(request)

    def delete(self, request):
        user = request.user
        try:
            cart_item = Basket.objects.get(pk=request.data.get('cart_item_pk'), user=user, order_yn=False)
        except Basket.DoesNotExist:
            data = {'error': '존재하지 않는 장바구니 속성입니다'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()

        return self.get(request)


class OrderView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        # IsUser,
    )

    def get(self, request):
        user = request.user
        bills = Bill.objects.filter(user=user).order_by('-order_date_time')
        serializer = OrderSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        address = request.data.get('address')
        delivery_date = request.data.get('delivery_date')
        order_item_list = request.data.get('order_item_list')
        total_price = request.data.get('total_price')
        try:
            bill = Bill.objects.create(
                user=user,
                address=address,
                delivery_date=delivery_date,
                total_price=total_price
            )
        except Bill.DoesNotExist:
            data ={
                'error': '입력한 조건으로 주문이 불가능 합니다'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        for order_item in order_item_list:
            cart_item_pk = order_item['cart_item_pk']
            try:
                order_item = Basket.objects.get(pk=cart_item_pk, user=user, order_yn=False)
            except Basket.DoesNotExist:
                data = {
                    'error': '장바구니에 존재하지 않는 item을 주문하려고 합니다'
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            order_item.order = bill
            order_item.order_yn = True
            order_item.save()
        return Response(OrderSerializer(bill).data, status=status.HTTP_200_OK)
