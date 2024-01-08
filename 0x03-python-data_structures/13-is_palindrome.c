#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *secondHalf;
	int palindrome = 1;

    /* Find the center of the list using the slow and fast pointers */
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/* Determine the starting point of the second half of the list */

	if (fast == NULL)
		secondHalf = slow; /* Even number of nodes */
	else
		secondHalf = slow->next; /* Odd number of nodes */

	/* Reverse the second half of the list */
	slow = NULL;
	while (secondHalf != NULL)
	{
		fast = secondHalf->next;
		secondHalf->next = slow;
		slow = secondHalf;
		secondHalf = fast;
	}
	secondHalf = slow;

    /* Compare the first and second parts of the list */
	slow = *head;
	fast = secondHalf;
	while (slow && fast)
	{
		if (slow->n != fast->n)
		{
			palindrome = 0; /* Not a palindrome if elements don't match */
			break;
		}
		slow = slow->next;
		fast = fast->next;
	}
    /* Reverse the second part of the list again and link it back to the first part */
	slow = NULL;
	while (secondHalf != NULL)
	{
		fast = secondHalf->next;
		secondHalf->next = slow;
		slow = secondHalf;
		secondHalf = fast;
	}
	secondHalf = slow;
    /* Return 1 if the list is a palindrome*/
	return  (palindrome);
}
