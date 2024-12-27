dataset=[]
dataset.append({"id": 1, "name": "matcha", "price": 90})
dataset.append({"id": 2, "name": "milktea", "price": 80})
dataset.append({"id": 3, "name": "coconut", "price": 70})



def print_data():
    for product in dataset:
        id=product["id"]
        name=product["name"]
        price=product["price"]
        infor=f"{id}\t{name}\t{price}"
        print(infor)

print_data
def sort_data():
    for i in range(0,len(dataset)):
        for j in range(i+1,len(dataset)):
            pi=dataset[i]
            pj=dataset[j]
            if pi["price"]>pj["price"]:
                dataset[i]=pj
                dataset[j]=pi
sort_data()
print("danh sách sản phẩm sau khi sắp xếp giá tăng dân:")
print_data()


def add_product():
    id=int(input("nhập mã:"))
    name=input("nhập tên:")
    price=float(input("nhập giá:"))
    product={"id": id, "name": "name", "price": price}
    dataset.append(product)
print(" mời bạn nhập sản phẩm mới:")
add_product()
print("danh sách san phẩm sau khi nhập mới:")
print_data()


dataset[0]={"id":113,"name":"coffee","price":20}
print("danh sách sản phẩm sau khi cập nhật:")
print_data()

dataset.pop(1)
print("danh sách sản phẩm sau khi xóa:")
print_data()
