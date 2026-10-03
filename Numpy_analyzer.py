import numpy as np

class DataAnalytics:
    def __init__(self):
        self.__oneD = None
        self.__twoD = None
        self.__threeD = None

    # --- Encapsulation: Getter and Setter Methods ---
    def get_oneD(self):
        return self.__oneD

    def set_oneD(self, *n):
        self.__oneD = np.array(n)
        print("Here is Your 1D Array:\n", self.__oneD)

    def get_twoD(self):
        return self.__twoD

    def set_twoD(self, rw, cl, *n):
        self.__twoD = np.array(n).reshape(rw, cl)
        print("Here is Your 2D Array:\n", self.__twoD)

    def get_threeD(self):
        return self.__threeD

    def set_threeD(self, dm, rw, cl, *n):
        self.__threeD = np.array(n).reshape(dm, rw, cl)
        print("Here is Your 3D Array:\n", self.__threeD)

    # --- Private Helper Method ---
    def __validate_array(self, choice):
        if choice == 1 and self.__oneD is not None:
            return self.__oneD
        elif choice == 2 and self.__twoD is not None:
            return self.__twoD
        elif choice == 3 and self.__threeD is not None:
            return self.__threeD
        else:
            print("Invalid choice or array not created yet.")
            return None

    # --- Indexing and Slicing ---
    def index_array(self, choice, *indices):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        if choice == 1:
            print("Indexed element from 1D Array:", arr[indices[0]])
        elif choice == 2:
            row, col = indices
            print("Indexed element from 2D Array:", arr[row, col])
        elif choice == 3:
            dm, rw, cl = indices
            print("Indexed element from 3D Array:", arr[dm, rw, cl])

    def slice_array(self, choice, *slices):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        if choice == 1:
            print("Sliced 1D Array:\n", arr[slices[0]])
        elif choice == 2:
            row_slice, col_slice = slices
            print("Sliced 2D Array:\n", arr[row_slice, col_slice])
        elif choice == 3:
            dm_slice, rw_slice, cl_slice = slices
            print("Sliced 3D Array:\n", arr[dm_slice, rw_slice, cl_slice])

    # --- Arithmetic operations ---
    def Addition(self, choice, *number):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        new_arr = np.array(number)
        if arr.size == new_arr.size:
            new_arr = new_arr.reshape(arr.shape)
            modify_arr = arr + new_arr
            print("Original Array:\n", arr)
            print("User given Array:\n", new_arr)
            print("Result of Addition:\n", modify_arr)
        else:
            print("Error: Array size mismatch.")

    def Subtraction(self, choice, *number):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        new_arr = np.array(number)
        if arr.size == new_arr.size:
            new_arr = new_arr.reshape(arr.shape)
            modify_arr = arr - new_arr
            print("Original Array:\n", arr)
            print("User given Array:\n", new_arr)
            print("Result of Subtraction:\n", modify_arr)
        else:
            print("Error: Array size mismatch.")

    def Multiplication(self, choice, *number):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        new_arr = np.array(number)
        if arr.size == new_arr.size:
            new_arr = new_arr.reshape(arr.shape)
            modify_arr = arr * new_arr
            print("Original Array:\n", arr)
            print("User given Array:\n", new_arr)
            print("Result of Multiplication:\n", modify_arr)
        else:
            print("Error: Array size mismatch.")

    def Division(self, choice, *number):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        new_arr = np.array(number)
        if arr.size == new_arr.size:
            new_arr = new_arr.reshape(arr.shape)
            modify_arr = arr / new_arr
            print("Original Array:\n", arr)
            print("User given Array:\n", new_arr)
            print("Result of Division:\n", modify_arr)
        else:
            print("Error: Array size mismatch.")

    # --- Combining arrays ---
    def combining(self, choice, *values):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        new = np.array(values)
        if choice == 1:
            if new.size == arr.size or new.ndim == 1:
                updated = np.concatenate((arr, new))
                print("Original Array:\n", arr)
                print("User Array:\n", new)
                print("Combined Array:\n", updated)
            else:
                print("Error: User array must be 1D")
        elif choice == 2:
            if new.size == arr.shape[1]:
                new = new.reshape(1, arr.shape[1])
                updated = np.vstack((arr, new))
                print("Original Array:\n", arr)
                print("User Array:\n", new)
                print("Combined Array:\n", updated)
            else:
                print("Error: User array must have", arr.shape[1], "columns")
        elif choice == 3:
            if new.size == np.prod(arr.shape[1:]):
                new = new.reshape(1, *arr.shape[1:])
                updated = np.concatenate((arr, new))
                print("Original Array:\n", arr)
                print("User Array:\n", new)
                print("Combined Array:\n", updated)
            else:
                print("Error: User array must have shape", arr.shape[1:])

    # --- Splitting arrays ---
    def split_array(self, choice, sections, axis=0):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        parts = np.array_split(arr, sections, axis=axis)
        print("Original Array:\n", arr)
        for i, p in enumerate(parts, 1):
            print(f"Part {i}:\n", p)

    # --- Searching for elements ---
    def search_array(self, choice, value):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        indices = np.argwhere(arr == value)
        print(f"Indices of {value}:\n", indices)

    # --- Sorting arrays ---
    def sort_array(self, choice, axis=-1):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        sorted_arr = np.sort(arr, axis=axis)
        print("Original Array:\n", arr)
        print(f"Sorted Array along axis {axis}:\n", sorted_arr)

    # --- User-defined filter ---
    def filter_array(self, choice, condition):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        filtered = arr[condition(arr)]
        print("Original Array:\n", arr)
        print("Filtered Array:\n", filtered)

    # --- Statistical operations ---
    def stats_array(self, choice, operation, axis=None, percentile_value=50):
        arr = self.__validate_array(choice)
        if arr is None:
            return
        print("Original Array:\n", arr)
        if operation == "sum":
            print("Sum:\n", np.sum(arr, axis=axis))
        elif operation == "mean":
            print("Mean:\n", np.mean(arr, axis=axis))
        elif operation == "median":
            print("Median:\n", np.median(arr, axis=axis))
        elif operation == "variance":
            print("Variance:\n", np.var(arr, axis=axis))
        elif operation == "correlation":
            if arr.ndim > 2:
                 print("Correlation is only supported for 1D or 2D arrays.")
            else:
               # For 2D arrays, correlation between columns is often more useful
               print("Correlation:\n", np.corrcoef(arr.T))
        elif operation == "percentile":
            print(f"{percentile_value}th Percentile:\n", np.percentile(arr, percentile_value, axis=axis))
        elif operation == "min":
            print("Minimum:\n", np.min(arr, axis=axis))
        elif operation == "max":
            print("Maximum:\n", np.max(arr, axis=axis))
        else:
            print("Invalid operation.")
    
    # --- Static Method ---
    @staticmethod
    def describe_array(arr):
        print(f"Shape: {arr.shape}, Dtype: {arr.dtype}, Dimensions: {arr.ndim}")


    @classmethod
    def from_random(cls, shape, seed=None):
        if seed is not None:
            np.random.seed(seed)
        arr = np.random.randint(1, 100, size=shape)
        print("Generated Random Array:\n", arr)
        obj = cls()
        if len(shape) == 1:
            obj.set_oneD(*arr)
        elif len(shape) == 2:
            obj.set_twoD(shape[0], shape[1], *arr.flatten())
        elif len(shape) == 3:
            obj.set_threeD(shape[0], shape[1], shape[2], *arr.flatten())
        return obj


# --- Menu System ---
def menu():
    da = DataAnalytics()
    while True:
        print("\n--- Welcome to the NumPy Analyzer! ---")
        print("==========================================")
        print("""
            choose an option:
            1.Create a Numpy Array
            2.Perform Mathematical Operations
            3.Indexing and Slicing
            4.Combining and Splitting Arrays
            5.Searching , Sorting and Filter
            6.Compute Statistical Operations
            7.Shape of all array
            8.Exit
            """)
        user = int(input("Enter your choice: "))

        if user == 1:
            print("""
                1. Create 1D Array
                2. Create 2D Array
                3. Create 3D Array
                """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                n = list(map(int, input("Enter elements for 1D array (space-separated): ").split()))
                da.set_oneD(*n)
            elif choice == 2:
                rw = int(input("Enter number of rows: "))
                cl = int(input("Enter number of columns: "))
                n = list(map(int, input(f"Enter {rw*cl} elements for 2D array (space-separated): ").split()))
                da.set_twoD(rw, cl, *n)
            elif choice == 3:
                dm = int(input("Enter number of dimensions: "))
                rw = int(input("Enter number of rows: "))
                cl = int(input("Enter number of columns: "))
                n = list(map(int, input(f"Enter {dm*rw*cl} elements for 3D array (space-separated): ").split()))
                da.set_threeD(dm, rw, cl, *n)
            else:
                print("Invalid choice.")

        elif user == 2:
            print("""
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                """)
            choice = int(input("Enter your choice : "))
            if choice == 1:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                n = list(map(int, input("Enter elements for addition according to the shape of array(space-separated): ").split()))
                da.Addition(arr_choice, *n)
            elif choice == 2:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                n = list(map(int, input("Enter elements for subtraction according to the shape of array(space-separated): ").split()))
                da.Subtraction(arr_choice, *n)
            elif choice == 3:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                n = list(map(int, input("Enter elements for multiplication according to the shape of array(space-separated): ").split()))
                da.Multiplication(arr_choice, *n)
            elif choice == 4:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                n = list(map(int, input("Enter elements for division according to the shape of array(space-separated): ").split()))
                da.Division(arr_choice, *n)
            else:
                print("Invalid choice.")
        
        elif user == 3:
            print("""
                1. Indexing
                2. Slicing
                """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                index = int(input("Enter index: "))
                da.index_array(arr_choice, index)
            elif choice == 2:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                slices = input("Enter slice indices (e.g., 'start:stop' or 'start:stop:step'): ")
                slice_tuple = tuple(slice(*map(int, s.split(':'))) for s in slices.split(','))
                da.slice_array(arr_choice, *slice_tuple)

        elif user == 4:
            print("""
                1. Combining Arrays
                2. Splitting Arrays
                """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                new_values = list(map(int, input("Enter elements to combine according to the shape of array (space-separated): ").split()))
                da.combining(arr_choice, *new_values)
            elif choice == 2:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                sections = int(input("Enter number of sections to split into: "))
                axis = int(input("Enter axis to split along (default 0): ") or 0)
                da.split_array(arr_choice, sections, axis)

        elif user == 5:
            print("""
                1. Searching
                2. Sorting
                3. Filtering
                """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                value = int(input("Enter value to search for: "))
                da.search_array(arr_choice, value)
            elif choice == 2:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                axis = int(input("Enter axis to sort along (-1 for last axis): "))
                da.sort_array(arr_choice, axis)
            elif choice == 3:
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                condition_str = input("""Enter condition for filtering 
                                        (e.g., 'lambda x: x > 10'): 
                                        (e.g., 'lambda x:x % 2 == 0' for even numbers): 
                                        (e.g., 'lambda x: x < 5' for less than 5): 
                                        (e.g., 'lambda x: x >= 15' for greater than or equal to 15):
                                        """)
                condition = eval(condition_str)
                da.filter_array(arr_choice, condition)
            else:
                print("Invalid choice.")   

        elif user == 6:
                print("""
                    1. Sum
                    2. Mean
                    3. Median
                    4. Variance
                    5. Correlation
                    6. Percentile
                    7. Minimum
                    8. Maximum
                """)
                choice = int(input("Enter your choice: "))
                arr_choice = int(input("Choose array (1D=1, 2D=2, 3D=3): "))
                axis = input("Enter axis (or leave blank for default): ")

                # Convert axis input to None if left blank
                axis = None if axis.strip() == "" else int(axis)

                # Map menu choice to operation string
                operations = {
                    1: "sum",
                    2: "mean",
                    3: "median",
                    4: "variance",
                    5: "correlation",
                    6: "percentile",
                    7: "min",
                    8: "max"
                }

                if choice in operations:
                  if choice == 6:  # Percentile
                   percentile_value = int(input("Enter percentile value or its by default 50 (e.g., 25, 50, 75): "))
                   da.stats_array(arr_choice, operations[choice], axis=axis, percentile_value=percentile_value)
                  else:
                     da.stats_array(arr_choice, operations[choice], axis=axis)
                else:
                         print("Invalid choice.")

        elif user == 7:
            print("Shape of 1D Array:", da.get_oneD().shape if da.get_oneD() is not None else "Not created")
            print("Shape of 2D Array:", da.get_twoD().shape if da.get_twoD() is not None else "Not created")
            print("Shape of 3D Array:", da.get_threeD().shape if da.get_threeD() is not None else "Not created")

if __name__ == "__main__":
    menu()

