#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: head of linked list
 * @number: data of new node
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;

	else if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		current = *head;
		while (current)
		{
			if (current->next == NULL && number != '\0')
			{
				current->next = new;
				break;
			}

			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				break;
			}

			current = current->next;
		}
	}
	return (new);
}
