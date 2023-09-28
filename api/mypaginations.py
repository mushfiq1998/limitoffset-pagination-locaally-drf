from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    # pass
    
    # Two records are shown in a single page
    default_limit = 2

    # Change default limit_query_param 'limit' to custom value 
    limit_query_param = 'mylimit'

    # Change default offset_query_param 'offset' to custom value 
    offset_query_param = 'myoffset'

    # Define maximum limit. 
    # It will not show more than three records in a single page 
    max_limit = 3
