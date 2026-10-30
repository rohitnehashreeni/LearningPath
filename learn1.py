Test = "first test case suite"

actual_result = 5

expected_result = 6

#ssert actual_result |xpected_result

print(f"{Test} : {actual_result == expected_result}")

# conditions in python

if actual_result == expected_result:
    print("test passed")
else:
    print("test failed")
    
#ex 1  
temprature = 29

if temprature >= 30:
    print ("hot")
elif temprature >= 20:
    print ("warm")
else:
    print("normal")
    
#ex 2
age = 18 
if age >=18: print("adult")
else: print("minor")

#ex 3
password = "abc123"
if password =="abc123": print("Access granted")
else: print("Access denied")

#ex 4
test_name = "login works"
expected = 25
actual = 6*4
passed = "test passed"
failed = "test failed"

if actual == expected: print(f"{test_name} : {passed}")
else: print(f"{test_name} : {failed}")

