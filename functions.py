import random
import string

from rest_framework.response import Response
from rest_framework import status


# defining function for random
# string id with parameter
def generate_id(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# def fetchProductDetails(product_id):
#     try:
#         product = Products.objects.get(pk=product_id)
#     except Products.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer = ProductSerializer(product)
#     return Response(serializer.name)