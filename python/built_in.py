#encoding=utf-8

def test_type_and_isinstance():
    class A:
        pass
    
    class B(A):
        pass
    a = A()
    b = B()
    print ('type(a) == A: {}'.format(type(a) == A))
    print ('type(b) == A: {}'.format(type(b) == A))
    print ('isinstance(a, A):{}'.format(isinstance(a, A)))
    print ('isinstance(b, A):{}'.format(isinstance(b, A)))

#test_type_and_isinstance()


def test_type_meta():
    class A:
        pass

    B = type('C', (object,), dict(c=1,d='1111'))
    print (B)
    a = B()
    print (a.d)
    print (type(A))

test_type_meta()

