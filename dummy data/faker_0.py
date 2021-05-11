from faker import Faker


fake = Faker("ko_KR")
for i in range(0,15):
    a = fake.address()
    print(a)
    # a = a.split(' ')
    # print(a[0]+a[1])
    