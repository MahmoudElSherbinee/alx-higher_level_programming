#include "lists.h"

/**
 * check_cycle - Checks for a cycle in a linked list
 * using Floyd's Tortoise and Hare algorithm
 * @head: Pointer to the head of the linked list
 *
 * This function checks if a linked list has a cycle
 * using Floyd's Tortoise and Hare algorithm.
 * Return: It returns 1 if a cycle is detected, otherwise returns 0.
 */

int check_cycle(listint_t *head)
{
	/* Step 1: Initialize two pointers, turtle and rabbit */
	listint_t *turtle = NULL;
	listint_t *rabbit = NULL;

	/* Step 2: Check if the list or its next node is NULL, */
	/* indicating an empty or single-node list */
	if (!head || !head->next)
		return (0);

	/* Step 3: Set initial positions for turtle and rabbit pointers */
	turtle = head;
	rabbit = head->next;

	/* Step 4: Iterate through the list using Floyd's */
	/* Tortoise and Hare algorithm */
	while (rabbit && rabbit->next)
	{
		/* Step 5: Move turtle pointer one step and rabbit pointer two steps */
		turtle = turtle->next;
		rabbit = rabbit->next->next;

		/* Step 6: Check if turtle and rabbit pointers meet, indicating a cycle */
		if (turtle == rabbit)
			return (1);
	}

	/* Step 7: If no cycle is found, return 0 */
	return (0);
}
