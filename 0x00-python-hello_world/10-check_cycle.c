#include "lists.h"

/**
 * check_cycle - function checks for a cycle in a linked list
 *
 * @list: Pointer to the head of the linked list
 *
 * This function checks if a linked list has a cycle.
 * Return: It returns 1 if a cycle is detected, otherwise returns 0.
 */
int check_cycle(listint_t *list)
{
	/* Step 1: Initialize a pointer to the head of the list */
	listint_t *now = list;

	/* Step 2: Check if the list or its next node is NULL, */
	/* indicating an empty or single-node list */
	if (!list || !list->next)
		return (0);

	/* Step 3: Iterate through the list using two pointers, */
	/* checking for a cycle */
	while (now->next)
	{
		/* Step 4: Check if the next node is equal to the head, indicating a cycle */
		if (now->next == list)
			return (1);

		/* Step 5: Move to the next node in the list */
		now = now->next;
	}

	/* Step 6: If no cycle is found, return 0 */
	return (0);
}
