#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "social.h"

Node *all_nodes[MAX_NODES]; // Array to store all nodes
int num_nodes = 0;          // Counter to keep track of total no. of nodes
int id = 1;                 // I have made the ID self incrementing i.e. it gets incremented and set as an ID of every new node created

// Function to create a node
Node *create_node(char *name, char type)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->id = id++;
    node->name = strdup(name);

    // Setting date and time to current date and time
    time_t currentTime;
    time(&currentTime);
    char *currentTimeString = ctime(&currentTime);
    node->date = strdup(currentTimeString);

    node->type = type;
    node->num_links = 0;
    node->links = NULL;
    node->num_contents = 0;
    node->content = NULL;

    return node;
}

// Function to create an individual
Individual *create_individual(char *name, char *birthday)
{
    Individual *individual = (Individual *)malloc(sizeof(Individual));
    individual->node = *create_node(name, 'I');
    individual->birthday = strdup(birthday);

    all_nodes[num_nodes++] = &individual->node;

    return individual;
}

// Function to create a business
Business *create_business(char *name, Location location)
{
    Business *business = (Business *)malloc(sizeof(Business));
    business->node = *create_node(name, 'B');
    business->location = location;
    business->num_owners = 0;
    business->num_customers = 0;

    all_nodes[num_nodes++] = &business->node;

    return business;
}

// Function to create a group
Group *create_group(char *name)
{
    Group *group = (Group *)malloc(sizeof(Group));
    group->node = *create_node(name, 'G');

    all_nodes[num_nodes++] = &group->node;

    return group;
}

// Function to create an organisation
Organisation *create_organisation(char *name, Location location)
{
    Organisation *organisation = (Organisation *)malloc(sizeof(Organisation));
    organisation->node = *create_node(name, 'O');
    organisation->location = location;

    all_nodes[num_nodes++] = &organisation->node;

    return organisation;
}

// Function to delete a node
void delete_node(char *name)
{
    SearchResult result = search_node_by_name(name);

    if (result.size == 0)
    {
        printf("Node not found\n");
    }
    else
    {
        printf("Node(s) found:\n");

        for (int i = 0; i < result.size; i++)
        {
            Node *current_node = result.nodes[i];

            for (int j = 0; j < num_nodes; j++)
            {
                if (j != current_node->id)
                {
                    remove_node_from_links(all_nodes[j], current_node);
                }
            }

            if (current_node->type == 'I')
            {
                Individual *individual = (Individual *)current_node;
                free(individual->birthday);
            }
            else if (current_node->type == 'B')
            {
                Business *business = (Business *)current_node;
                free(business->owners);
                free(business->customers);
            }
            else if (current_node->type == 'G')
            {
                Group *group = (Group *)current_node;
                free(group->members);
            }
            else if (current_node->type == 'O')
            {
                Organisation *organisation = (Organisation *)current_node;
                free(organisation->members);
            }

            free(current_node->date);
            free(current_node->name);
            free(current_node->links);
            free(current_node->content);
            free(current_node);
            num_nodes--;
        }

        printf("Node(s) deleted\n");
    }

    free(result.nodes);
}

// Function to remove a node from the links of another node
void remove_node_from_links(Node *node, Node *target)
{
    for (int i = 0; i < node->num_links; i++)
    {
        if (node->links[i] == target)
        {
            for (int j = i; j < node->num_links - 1; j++)
            {
                node->links[j] = node->links[j + 1];
            }
            node->num_links--;
            break;
        }
    }
}

// Function to search node by name
SearchResult search_node_by_name(char *name)
{
    SearchResult result;
    result.nodes = (Node **)malloc(num_nodes * sizeof(Node *));
    result.size = 0;

    for (int i = 0; i < num_nodes; i++)
    {
        if (strcmp(all_nodes[i]->name, name) == 0)
        {
            result.nodes[result.size++] = all_nodes[i];
        }
    }

    result.nodes = realloc(result.nodes, result.size * sizeof(Node *));
    return result;
}

// Function to search node by type
SearchResult search_node_by_type(char type)
{
    SearchResult result;
    result.nodes = (Node **)malloc(num_nodes * sizeof(Node *));
    result.size = 0;

    for (int i = 0; i < num_nodes; i++)
    {
        if (all_nodes[i]->type == type)
        {
            result.nodes[result.size++] = all_nodes[i];
        }
    }

    result.nodes = realloc(result.nodes, result.size * sizeof(Node *));
    return result;
}

// Function to search individual by birthday
SearchResult search_individual_by_birthday(char *birthday)
{
    SearchResult result;
    result.nodes = (Node **)malloc(num_nodes * sizeof(Node *));
    result.size = 0;

    for (int i = 0; i < num_nodes; i++)
    {
        if (all_nodes[i]->type == 'I' && strcmp(((Individual *)all_nodes[i])->birthday, birthday) == 0)
        {
            result.nodes[result.size++] = all_nodes[i];
        }
    }

    result.nodes = realloc(result.nodes, result.size * sizeof(Node *));
    return result;
}

// Function to check if a link between two nodes already exists
int is_node_in_links(Node *node, Node *target)
{
    for (int i = 0; i < node->num_links; i++)
    {
        if (node->links[i] == target)
        {
            return 1;
        }
    }
    return 0;
}

// Function to add members in groups and organisations
void add_member(Node *group_or_org, Node *new_member)
{
    if (group_or_org->type == 'O' && new_member->type != 'I')
    {
        printf("Only individuals can be added to organisations.\n");
        return;
    }

    if (!is_node_in_links(group_or_org, new_member))
    {
        group_or_org->links = realloc(group_or_org->links, (group_or_org->num_links + 1) * sizeof(Node *));
        if (!group_or_org->links)
        {
            printf("Failed to allocate memory for new link.\n");
            return;
        }

        group_or_org->links[group_or_org->num_links] = new_member;
        group_or_org->num_links++;
    }

    if (!is_node_in_links(new_member, group_or_org))
    {
        new_member->links = realloc(new_member->links, (new_member->num_links + 1) * sizeof(Node *));
        if (!new_member->links)
        {
            printf("Failed to allocate memory for new link.\n");
            return;
        }

        new_member->links[new_member->num_links] = group_or_org;
        new_member->num_links++;
    }

    for (int i = 0; i < group_or_org->num_links; i++)
    {
        if (group_or_org->links[i] != new_member && group_or_org->links[i]->type == 'I')
        {
            if (!is_node_in_links(group_or_org->links[i], new_member))
            {
                group_or_org->links[i]->links = realloc(group_or_org->links[i]->links, (group_or_org->links[i]->num_links + 1) * sizeof(Node *));
                if (!group_or_org->links[i]->links)
                {
                    printf("Failed to allocate memory for new link.\n");
                    return;
                }

                group_or_org->links[i]->links[group_or_org->links[i]->num_links] = new_member;
                group_or_org->links[i]->num_links++;

                new_member->links = realloc(new_member->links, (new_member->num_links + 1) * sizeof(Node *));
                if (!new_member->links)
                {
                    printf("Failed to allocate memory for new link.\n");
                    return;
                }

                new_member->links[new_member->num_links] = group_or_org->links[i];
                new_member->num_links++;
            }
        }
    }
}

// Function to add an owner or customer to a business
void add_owner_or_customer(Business *business, Individual *new_owner_or_customer, char role)
{
    if (role == 'O' || role == 'C')
    {
        for (int i = 0; i < business->node.num_links; i++)
        {
            if (business->node.links[i] == &new_owner_or_customer->node)
            {
                printf("Node is already a link.\n");
                return;
            }
        }

        business->node.links = realloc(business->node.links, (business->node.num_links + 1) * sizeof(Node *));
        if (!business->node.links)
        {
            printf("Failed to allocate memory for new link.\n");
            return;
        }

        business->node.links[business->node.num_links] = &new_owner_or_customer->node;
        business->node.num_links++;

        if (role == 'O')
        {
            business->owners = realloc(business->owners, (business->num_owners + 1) * sizeof(Individual *));
            if (!business->owners)
            {
                printf("Failed to allocate memory for new owner.\n");
                return;
            }

            business->owners[business->num_owners] = new_owner_or_customer;
            business->num_owners++;
            printf("Node(s) added as owner(s) successfully.\n");
        }
        else
        {
            business->customers = realloc(business->customers, (business->num_customers + 1) * sizeof(Individual *));
            if (!business->customers)
            {
                printf("Failed to allocate memory for new customer.\n");
                return;
            }

            business->customers[business->num_customers] = new_owner_or_customer;
            business->num_customers++;
            printf("Node(s) added as customer(s) successfully.\n");
        }
    }
    else
    {
        printf("Invalid role. Role must be 'O' for owner or 'C' for customer.\n");
    }
}

// Function to print the linked nodes of a node
void print_linked_nodes(char *name)
{
    int flag = 0;
    for (int i = 0; i < num_nodes; i++)
    {
        if (strcmp(all_nodes[i]->name, name) == 0)
        {
            flag = 1;
            for (int j = 0; j < all_nodes[i]->num_links; j++)
            {
                printf("Linked node: %s\n", all_nodes[i]->links[j]->name);
            }
            return;
        }
    }
    if (flag == 0)
    {
        printf("Node not found\n");
    }
}

// Function to post content on a node
void post_content(char *name, char *content)
{
    SearchResult result = search_node_by_name(name);

    if (result.size == 0)
    {
        printf("Node not found\n");
    }
    else
    {
        printf("Node(s) found:\n");

        for (int i = 0; i < result.size; i++)
        {
            Node *current_node = result.nodes[i];

            current_node->content = realloc(current_node->content, (current_node->num_contents + 1) * sizeof(char *));
            if (!current_node->content)
            {
                printf("Failed to allocate memory for new content.\n");
                return;
            }

            current_node->content[current_node->num_contents] = strdup(content);
            current_node->num_contents++;
        }

        printf("Content posted to node(s)\n");
    }

    free(result.nodes);
}

// Function to search and print the content posted by a node
void search_and_print_content(char *name)
{
    SearchResult result = search_node_by_name(name);

    if (result.size == 0)
    {
        printf("Node not found\n");
    }
    else
    {
        printf("Node(s) found:\n");

        for (int i = 0; i < result.size; i++)
        {
            Node *current_node = result.nodes[i];

            printf("Content of node %s:\n", current_node->name);
            for (int j = 0; j < current_node->num_contents; j++)
            {
                printf("%s\n", current_node->content[j]);
            }
        }
    }

    free(result.nodes);
}

// Function to print the content posted by linked nodes of a node
void display_linked_content(char *name)
{
    SearchResult result = search_node_by_name(name);

    if (result.size == 0)
    {
        printf("Node not found\n");
    }
    else
    {
        printf("Node(s) found:\n");

        for (int i = 0; i < result.size; i++)
        {
            Node *current_node = result.nodes[i];

            printf("Content linked to %s:\n", current_node->name);
            for (int j = 0; j < current_node->num_links; j++)
            {
                printf("Content posted by %s:\n", current_node->links[j]->name);
                for (int k = 0; k < current_node->links[j]->num_contents; k++)
                {
                    printf("%s\n", current_node->links[j]->content[k]);
                }
            }
        }
    }

    free(result.nodes);
}

// Function to print the details of a node
void print_node_details(Node *node)
{
    printf("Node details:\n");
    printf("ID: %d\n", node->id);
    printf("Name: %s\n", node->name);

    printf("Type: ");
    if (node->type == 'I')
        printf("Individual\n");
    else if (node->type == 'G')
        printf("Group\n");
    else if (node->type == 'B')
        printf("Business\n");
    else if (node->type == 'O')
        printf("Organisation\n");

    printf("Date of creation: %s\n", node->date);
}

// Function to print all nodes
void print_all_nodes()
{
    for (int i = 0; i < num_nodes; i++)
    {
        printf("Node %d:\n", i + 1);
        print_node_details(all_nodes[i]);
        printf("\n");
    }
}

// Master text-based interface
void interface()
{
    while (1)
    {
        printf("\nSelect any of the following:\n");
        printf("1. Create node\n");
        printf("2. Delete node\n");
        printf("3. Search node\n");
        printf("4. Print linked nodes\n");
        printf("5. Post content\n");
        printf("6. Search for content\n");
        printf("7. Display all content posted by linked nodes\n");
        printf("8. Print all nodes\n");
        printf("9. Exit\n");

        int choice;
        scanf("%d", &choice);

        if (choice == 1)
        {
            char type;
            printf("Enter type: (I- individual, G- Group, B- Business, O- Organisation) ");
            scanf(" %c", &type);

            if (type == 'I')
            {
                char name[100], birthday[100];
                printf("Enter name: ");
                scanf("%s", name);
                printf("Does this individual have a birthday? Y/N: ");
                char yesno;
                scanf(" %c", &yesno);
                if (yesno == 'Y')
                {
                    printf("Enter birthday: ");
                    scanf("%s", birthday);
                    create_individual(name, birthday);
                }
                else
                {
                    create_individual(name, "NULL");
                }
            }

            if (type == 'G')
            {
                char name[100];
                printf("Enter name: ");
                scanf("%s", name);
                Group *group = create_group(name);
                int group_id = group->node.id;

                printf("Does your group have members? Y/N : ");
                char yesno;
                scanf(" %c", &yesno);
                if (yesno == 'Y')
                {
                    printf("Enter number of members: ");
                    int num_members;
                    scanf("%d", &num_members);
                    for (int i = 0; i < num_members; i++)
                    {
                        printf("Do you want to add new nodes or existing nodes as members? N- new nodes, E- existing nodes: ");
                        char choice;
                        scanf(" %c", &choice);
                        if (choice == 'N')
                        {
                            char type;
                            printf("Enter type of new member: (I- individual, B- Business) ");
                            scanf(" %c", &type);

                            if (type == 'I')
                            {
                                char name[100], birthday[100];
                                printf("Enter name: ");
                                scanf("%s", name);
                                printf("Does this individual have a birthday? Y/N: ");
                                char yesno;
                                scanf(" %c", &yesno);
                                if (yesno == 'Y')
                                {
                                    printf("Enter birthday: ");
                                    scanf("%s", birthday);
                                    create_individual(name, birthday);
                                }
                                else
                                {
                                    create_individual(name, "NULL");
                                }

                                add_member(all_nodes[group_id - 1], all_nodes[num_nodes - 1]);
                            }

                            else if (type == 'B')
                            {
                                char name[100];
                                Location location;
                                printf("Enter name, location (x y): ");
                                scanf("%s %lf %lf", name, &location.x, &location.y);
                                create_business(name, location);

                                add_member(all_nodes[group_id - 1], all_nodes[num_nodes - 1]);
                            }
                        }
                        else if (choice == 'E')
                        {
                            char name[100];
                            printf("Enter name of node to add as member: ");
                            scanf("%s", name);
                            SearchResult result = search_node_by_name(name);

                            if (result.size == 0)
                            {
                                printf("Node not found\n");
                            }
                            else
                            {
                                printf("Node(s) found:\n");

                                for (int i = 0; i < result.size; i++)
                                {
                                    Node *current_node = result.nodes[i];

                                    add_member(all_nodes[group_id - 1], current_node);
                                }

                                printf("Node(s) added as member(s)\n");
                            }

                            free(result.nodes);
                        }
                    }
                }
            }

            if (type == 'B')
            {
                char name[100];
                Location location;
                printf("Enter name, location (x y): ");
                scanf("%s %lf %lf", name, &location.x, &location.y);
                Business *business = create_business(name, location);

                printf("Does your business have owners? Y/N : ");
                char yesno;
                scanf(" %c", &yesno);
                if (yesno == 'Y')
                {
                    printf("Enter number of owners: ");
                    int num_owners;
                    scanf("%d", &num_owners);
                    for (int i = 0; i < num_owners; i++)
                    {
                        printf("Do you want to add a new individual as owner or an existing individual? N- new, E- existing: ");
                        char choice;
                        scanf(" %c", &choice);

                        if (choice == 'N')
                        {
                            char name[100], birthday[100];
                            printf("Enter name: ");
                            scanf("%s", name);
                            printf("Does this individual have a birthday? Y/N: ");
                            char yesno;
                            scanf(" %c", &yesno);
                            if (yesno == 'Y')
                            {
                                printf("Enter birthday: ");
                                scanf("%s", birthday);
                                create_individual(name, birthday);
                            }
                            else
                            {
                                create_individual(name, "NULL");
                            }

                            add_owner_or_customer(business, (Individual *)all_nodes[num_nodes - 1], 'O');
                        }
                        else if (choice == 'E')
                        {
                            char name[100];
                            printf("Enter name of node to add as owner: ");
                            scanf("%s", name);
                            SearchResult result = search_node_by_name(name);

                            if (result.size == 0)
                            {
                                printf("Node not found\n");
                            }
                            else
                            {
                                printf("Node(s) found:\n");

                                for (int i = 0; i < result.size; i++)
                                {
                                    Node *current_node = result.nodes[i];

                                    add_owner_or_customer(business, (Individual *)current_node, 'O');
                                }
                            }

                            free(result.nodes);
                        }
                    }
                }

                printf("Does your business have customers? Y/N : ");
                scanf(" %c", &yesno);
                if (yesno == 'Y')
                {
                    printf("Enter number of customers: ");
                    int num_customers;
                    scanf("%d", &num_customers);
                    for (int i = 0; i < num_customers; i++)
                    {
                        printf("Do you want to add a new individual as customer or an existing individual? N- new, E- existing: ");
                        char choice;
                        scanf(" %c", &choice);
                        if (choice == 'N')
                        {
                            char name[100], birthday[100];
                            printf("Enter name: ");
                            scanf("%s", name);
                            printf("Does this individual have a birthday? Y/N: ");
                            char yesno;
                            scanf(" %c", &yesno);
                            if (yesno == 'Y')
                            {
                                printf("Enter birthday: ");
                                scanf("%s", birthday);
                                create_individual(name, birthday);
                            }
                            else
                            {
                                create_individual(name, "NULL");
                            }

                            add_owner_or_customer(business, (Individual *)all_nodes[num_nodes - 1], 'C');
                        }
                        else if (choice == 'E')
                        {
                            char name[100];
                            printf("Enter name of node to add as customer: ");
                            scanf("%s", name);
                            SearchResult result = search_node_by_name(name);

                            if (result.size == 0)
                            {
                                printf("Node not found\n");
                            }
                            else
                            {
                                printf("Node(s) found:\n");

                                for (int i = 0; i < result.size; i++)
                                {
                                    Node *current_node = result.nodes[i];

                                    add_owner_or_customer(business, (Individual *)current_node, 'C');
                                }

                                printf("Node(s) added as customer(s)\n");
                            }

                            free(result.nodes);
                        }
                    }
                }
            }

            if (type == 'O')
            {
                char name[100];
                Location location;
                printf("Enter name, location (x y): ");
                scanf("%s %lf %lf", name, &location.x, &location.y);
                Organisation *organisation = create_organisation(name, location);
                int organisation_id = organisation->node.id;

                printf("Does your organisation have members (Only individuals allowed) ? Y/N: ");
                char yesno;
                scanf(" %c", &yesno);
                if (yesno == 'Y')
                {
                    printf("Enter number of members: ");
                    int num_members;
                    scanf("%d", &num_members);
                    for (int i = 0; i < num_members; i++)
                    {
                        printf("Do you want to add a new individual as member or an existing individual? N- new, E- existing: ");
                        char choice;
                        scanf(" %c", &choice);
                        if (choice == 'N')
                        {
                            char name[100], birthday[100];
                            printf("Enter name: ");
                            scanf("%s", name);
                            printf("Does this individual have a birthday? Y/N: ");
                            char yesno;
                            scanf(" %c", &yesno);
                            if (yesno == 'Y')
                            {
                                printf("Enter birthday: ");
                                scanf("%s", birthday);
                                create_individual(name, birthday);
                            }
                            else
                            {
                                create_individual(name, "NULL");
                            }

                            add_member(all_nodes[organisation_id - 1], all_nodes[num_nodes - 1]);
                        }
                        else if (choice == 'E')
                        {
                            char name[100];
                            printf("Enter name of node to add as member: ");
                            scanf("%s", name);
                            SearchResult result = search_node_by_name(name);

                            if (result.size == 0)
                            {
                                printf("Node not found\n");
                            }
                            else
                            {
                                printf("Node(s) found:\n");

                                for (int i = 0; i < result.size; i++)
                                {
                                    Node *current_node = result.nodes[i];

                                    add_member(all_nodes[organisation_id - 1], current_node);
                                }

                                printf("Node(s) added as member(s)\n");
                            }

                            free(result.nodes);
                        }
                    }
                }
            }
        }
        else if (choice == 2)
        {
            char name[100];
            printf("Enter name of node to delete: ");
            scanf("%s", name);
            delete_node(name);
        }
        else if (choice == 3)
        {
            printf("Do you want to search by name, type or birthday (for individual only)? N- name, T- type, B- birthday: ");
            char choice;
            scanf(" %c", &choice);
            if (choice == 'N')
            {
                char name[100];
                printf("Enter name: ");
                scanf("%s", name);
                SearchResult result = search_node_by_name(name);
                if (result.size == 0)
                {
                    printf("Node not found\n");
                }
                else
                {
                    printf("Node(s) found:\n");

                    for (int i = 0; i < result.size; i++)
                    {
                        Node *current_node = result.nodes[i];

                        print_node_details(current_node);
                    }
                }
            }
            else if (choice == 'T')
            {
                char type;
                printf("Enter type: ");
                scanf(" %c", &type);
                SearchResult result = search_node_by_type(type);
                if (result.size == 0)
                {
                    printf("Node not found\n");
                }
                else
                {
                    printf("Node(s) found:\n");

                    for (int i = 0; i < result.size; i++)
                    {
                        Node *current_node = result.nodes[i];

                        print_node_details(current_node);
                    }
                }
            }
            else if (choice == 'B')
            {
                char birthday[100];
                printf("Enter birthday: ");
                scanf("%s", birthday);
                SearchResult result = search_individual_by_birthday(birthday);
                if (result.size == 0)
                {
                    printf("Node not found\n");
                }
                else
                {
                    printf("Node(s) found:\n");

                    for (int i = 0; i < result.size; i++)
                    {
                        Node *current_node = result.nodes[i];

                        print_node_details(current_node);
                    }
                }
            }
        }
        else if (choice == 4)
        {
            char name[100];
            printf("Enter name of node: ");
            scanf("%s", name);
            print_linked_nodes(name);
        }
        else if (choice == 5)
        {
            char name[100], content[100];
            printf("Enter name of node and content to post: ");
            scanf("%s %s", name, content);
            post_content(name, content);
        }
        else if (choice == 6)
        {
            char name[100];
            printf("Enter name of node: ");
            scanf("%s", name);
            search_and_print_content(name);
        }
        else if (choice == 7)
        {
            char name[100];
            printf("Enter name of node: ");
            scanf("%s", name);
            display_linked_content(name);
        }
        else if (choice == 8)
        {
            print_all_nodes();
        }
        else if (choice == 9)
        {
            break;
        }
    }
}

int main()
{
    interface();

    return 0;
}