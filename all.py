def acad_zip(*iterables, strict=False):
    iterators = [iter(iterable) for iterable in iterables]
    while True:
        try:
            current_tuple = tuple(next(iterator) for iterator in iterators)
            yield current_tuple
        except StopIteration:
            return


def academy_map( func, *iterables):
    iterators = [iter(iterator) for iterator in iterables]
    while True:
        try:
            current_tuple = [next(iterator) for iterator in iterators]
            yield func(current_tuple)
        except StopIteration:
            return


def acadd_enumerate(iterable, start=0):
    for item in iterable:
        yield start, item
        start +=1


def acad_filter(func,iterable):
    if func is None:
        filtered_items = [i for i in iterable if bool(i)]
    else:
        filtered_items = [i for i in iterable if func(i)]
    for item in filtered_items:
        return item


def academy_reduce(func,iterable,initial = None):
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