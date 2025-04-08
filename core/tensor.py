#             #
#   TENSORS   #
#             #



class Tensor:
    def __init__(self, data, requires_grad=False):
        self.data = _ensure_tensor_data(data) # the data we are storing in our tensor
        self.requires_grad = requires_grad # store how this tensor effects the final result
        self.grad = None # affekt on final result
        self.grad_fn = None # step to do the backwards()
        self.children = None # tensors used to create this tensor
        self._shape = self._calculate_shape(self.data) # shape of the tensor like dimenseions for example 3x3


    def _ensure_tensor_data(self, data):
        if isinstance(data, (int, float)):
            return data
        elif isinstance(data, list):
            if all(isinstance(item, (int, float)) for item in data):
                return data
            elif isinstance((item, list) for item in data):
                return [self._ensure_tensor_data(item) for item in data]
            else :
                raise TypeError("data must be int or float")
        elif isinstance(data, Tensor):
            return self._ensure_tensor_data(data.data)
        else:
            raise TypeError("data must be int or float")

    def _calculate_shape(self, data):
        if isinstance(data, (int, float)):
            return ()

        shape = [len(data)]
        if data and isinstance(data[0], list):
            inner_shape = self._calculate_shape(data[0])
            shape.extend(inner_shape)

        return tuple(shape)








list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]
list5 = [13, 14, 15]

tensor = Tensor(data=[list1, list2, list3, list4, list5])

print(tensor._shape)
print(tensor)


