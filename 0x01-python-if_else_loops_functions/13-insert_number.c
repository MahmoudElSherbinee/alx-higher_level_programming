#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - Function inserts a new node with the
 * given number into a sorted linked list.
 *
 * This function takes a pointer to the head of a
 * sorted linked list and a number.
 * It creates a new node with the given number\
 * and inserts it into the linked list
 * while maintaining the ascending order of the list.
 *
 * @head: A pointer to the head of the linked list.
 * @number: The number to be inserted into the linked list.
 *
 * Return: A pointer to the newly inserted node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	/* Step 1: Initialize pointers for current, new, and temporary nodes */
	listint_t *current_node = *head;
	listint_t *new_node = NULL;
	listint_t *temp_node = NULL;

	/* Step 2: Check if the head pointer is valid */
	if (!head)
		return (NULL);

	/* Step 3: Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	/* Step 4: Set values for the new node */
	new_node->n = number;
	new_node->next = NULL;

	/* Step 5: Insert the new node at the beginning if the list is empty */
	/* or the number is smaller than the head's number */
	if (!*head || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		/* Step 6: Traverse the list to find the correct position for insertion */
		while (current_node && current_node->n < number)
		{
			temp_node = current_node;
			current_node = current_node->next;
		}

		/* Step 7: Insert the new node between temp_node and current_node */
		temp_node->next = new_node;
		new_node->next = current_node;
	}
	/* Step 8: Return a pointer to the newly inserted node */
	return (new_node);
}
