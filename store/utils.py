import json
from . models import *

def cookieCart(request):
    try:
        #loading cookies
        cart =  json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        #print("CCCCCCCCCCCCCookie",cart)
    #list for keeping item info in it for displaying purpose without using database
    items=[] 
    doneorditem ={}
    order={'get_cart_items':0,'get_cart_total':0,'shipping':False}
    cartItems=order['get_cart_items']

    # updating total as items added into the cookies for AnonymousUser
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            order['get_cart_total']+=total
            order['get_cart_items']+=cart[i]['quantity']

            item = {
                    'product':{
                                    'id':product.id,
                                    'name':product.name,
                                    'price':product.price,
                                    'imageURL':product.imageURL
                            },
                    'quantity':cart[i]['quantity'],
                    'get_total':total
                }
            items.append(item)
            
            if product.digital == False:
                order['shipping'] = True
        except:
           
            pass
        
    return {'cartItems':cartItems,'order':order,'items':items,'doneorditem':doneorditem}


def cartData(request):
    loginflag = False
    if request.user.is_authenticated:
        customer = Customer.objects.get_or_create(user=request.user,name=request.user.username,email=request.user.email)
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        
        try:
            doneorditem = []
            for preorders in Order.objects.filter(customer=customer,complete=True):
                orderitems = OrderItem.objects.get(order=preorders)
                doneorditem.append(orderitems)
        except:
            doneorditem = []
        items = order.orderitem_set.all()
        loginflag = True
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        doneorditem = cookieData['doneorditem']
    return {'cartItems':cartItems,'order':order,'items':items,'loginflag':loginflag,'doneorditem':doneorditem}