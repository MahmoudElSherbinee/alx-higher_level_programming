#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function print information about a Python list.
 * @p:   A pointer to a PyObject representing a Python list.
 */

void print_python_list_info(PyObject *p)
{
	int i, size;
	PyListObject *list;

	/* Step 1: Get the size of the Python list */
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);

	/* Step 2: Obtain the allocated space for the list */
	list = (PyListObject *)p;
	printf("[*] Allocated = %d\n", (int)list->allocated);

	/* Step 3: Iterate through the list*/
	/* and print information about each element */
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
