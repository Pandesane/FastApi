

from models.product import Product
from models.shop import Shop
from models.user import User,Gender


products = [
    Product(
        category='Electronics',
        description='Great Product Here',
        ID='1',
        imageUrl='',
        minimumOrder=10,
        name='Samsung Galaxy 13',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='2',
        imageUrl='',
        minimumOrder=10,
        name='Samsung Galaxy 14',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='3',
        imageUrl='',
        minimumOrder=10,
        name='Samsung note 11',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='4',
        imageUrl='',
        minimumOrder=10,
        name='Samsung 454',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Samsung note 20',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Samsung Fire 2',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Bubble Screen',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Iphone',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Nokia',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Tecno',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Raspberry Pi',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Tecno Infinix',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Dell PC',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Mac book',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Lenovo',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Iphone 14',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='Oppo 88',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ), Product(
        category='Electronics',
        description='Great Product Here',
        ID='1223',
        imageUrl='',
        minimumOrder=10,
        name='UGL 23',
        numberInStock=10,
        price=100,
        productSpecifications=[],

        tags=[],
        videoUrl=''


    ),
]

user = User(
    contact='+256740412350',
    email='stevoxsanedagreat@gmail.com',
    firstName='Stephen',
    lastName='Pande',
    location='Pallisa',
    password='1234567890',
     gender= Gender.MALE
)
shop = Shop(

    owner=user,
    products= products,
    services=[]
)
