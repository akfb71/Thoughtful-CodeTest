
def sort(width,height,length,mass):
  if width*height*length >= 1000000 or width>=150 or height>=150 or length>=150:
    if mass>=20:
      #both heavy and bulky
      return "REJECTED"
    else:
      #only bulky
      return "SPECIAL"
  elif mass>=20:
    #only heavy
    return "SPECIAL"
  #neither heavy nor bulky
  return "STANDARD"


def test_sort():
  # Neither heavy nor bulky
  assert sort(10, 10, 10, 5) == "STANDARD"
  assert sort(99, 99, 99, 19.9) == "STANDARD"

  # Only bulky
  assert sort(200, 100, 100, 10) == "SPECIAL"
  assert sort(100, 200, 100, 10) == "SPECIAL"
  assert sort(100, 100, 200, 10) == "SPECIAL"
  assert sort(1000, 1000, 1, 10) == "SPECIAL"

  # Only heavy
  assert sort(10, 10, 10, 20) == "SPECIAL"
  assert sort(100, 100, 90, 25) == "SPECIAL"

  # Both bulky and heavy
  assert sort(150, 100, 100, 20) == "REJECTED"
  assert sort(100, 100, 1000, 50) == "REJECTED"
  assert sort(1000, 1000, 1, 25) == "REJECTED"

  # Edge cases
  assert sort(150, 100, 100, 19.9) == "SPECIAL"
  assert sort(100, 100, 100, 20) == "SPECIAL"
  assert sort(100, 100, 100, 19.9) == "STANDARD"
  assert sort(100, 100, 100, 20.0) == "SPECIAL"
  assert sort(150, 100, 100, 20.0) == "REJECTED"

  # min-max values
  assert sort(10000, 10000, 10000, 1000) == "REJECTED"
  assert sort(0, 0, 0, 0) == "STANDARD"

  print("All test cases passed!")

test_sort()
