

# def my_zip(*iterables, strict=False):
#doesnt work right
#     iterators = [iter(iterable) for iterable in iterables]
#     while True:
#         try:
#             current_tuple = tuple(next(iterator) for iterator in iterators)
#             yield current_tuple
#         except StopIteration:
#             return
            
def my_zip(*iterables, strict=False):  
  iterators = [iter(it) for it in iterables]
  res = []
  while True:
    try:
      res.append(tuple([next(it) for it in iterators]))
      print("no exception")
    except StopIteration:
      print("exception")
      break
  return res            


def my_map( func, *iterables):
    iterators = [iter(iterator) for iterator in iterables]
    while True:
        try:
            current_tuple = [next(iterator) for iterator in iterators]
            yield func(current_tuple)
        except StopIteration:
            return


def my_enumerate(iterable, start=0):
    for item in iterable:
        yield start, item
        start +=1


def my_filter(func,iterable):
    if func is None:
        filtered_items = [i for i in iterable if bool(i)]
    else:
        filtered_items = [i for i in iterable if func(i)]
    for item in filtered_items:
        return item


def my_reduce(func,iterable,initial = None):
    iterator = iter(iterable)
    if initial is None:
        try:
            initial = next(iterator)
        except TypeError:
            raise"reduce() of it with no initial value"
    res = initial
    for item in iterator:
        res = func(res,item)

    return res
