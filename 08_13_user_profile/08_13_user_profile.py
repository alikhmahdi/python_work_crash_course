def user_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    user_info['first']=first
    user_info['last']=last
    return user_info
print(user_profile('mahdi', 'alikhani', location='tehran', field='programming', age=17))