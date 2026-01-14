#---------------------------------------------File not found error-----------------------------------------------------#

try:                                                # What should have happened. But the file does not exist.
    file =open("a_file.txt")

except FileNotFoundError:
                                                    #  Try this if exception. But want it to catch a specific error.
                                                    #  Can have multiple errors as well.
    file = open("a_file.txt", "w")

except KeyError as error_message:
                                                    # Can get a hold pof the error message by the use of as
    print(f"The key {error_message} does not exist!")

else:
                                                    # Else Block does not occur - moves onto the exceppt block.
                                                    # Then second time round it will trigger the else block
    content  = file.read()

finally:
    file.close()                                    # Run it no matter what


    raise KeyError

