def largest_sum(numbers: list[int]) -> tuple[int, int]:
    primeiro = 0 
    segundo = 0
    numbers.sort()
    if len(numbers) < 2:
        return None
    else:

     primeiro = numbers[-2]
     segundo = numbers[-1]
    

     return primeiro, segundo
