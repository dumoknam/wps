from rest_framework import serializers

from items.models import Item
from items.restful_serializers import ItemsSimpleSerializer
from members.restful_serializers import UserSerializer
from .models import Basket, Bill


class BasketListSerializer(serializers.ModelSerializer):
    item = ItemsSimpleSerializer()

    class Meta:
        model = Basket
        fields = ('pk', 'user', 'item', 'amount')


class BasketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Basket
        fields = ('pk', 'user', 'item', 'amount')
        read_only_fields = ('user',)

    def validate(self, data):
        data
        if Basket.objects.filter(item=data['item'], user=data['user'], order_yn=False).exists():
            raise serializers.ValidationError('이미 장바구니에 존재하는 반찬입니다')
        return data

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError('주문량이 0보다 작습니다')
        return value







class OrderSerializer(serializers.ModelSerializer):
    user_pk = serializers.CharField(source='user.pk')
    cart_items = BasketListSerializer(source='basket_set', many=True)
    order_pk = serializers.CharField(source='pk')

    class Meta:
        model = Bill
        fields = (
            'order_pk',
            'user_pk',
            'order_date_time',
            'delivery_date',
            'total_price',
            'cart_items',
        )
        read_only_fields = ('cart_items', 'order_pk')








