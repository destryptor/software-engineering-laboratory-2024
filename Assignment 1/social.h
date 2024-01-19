/*
    Program Description:

    This program implements a simple social network system with support for individuals, businesses, groups, and organizations. It uses various structures and functions to create, manage, and interact with nodes representing entities in the social network.

    Structures:

    1. Node:
       - Represents a generic node in the social network with essential information such as ID, links to other nodes, name, date, content, and type (individual, business, group, or organization).

    2. Individual:
       - Inherits from Node and adds specific information for individuals, such as birthday.

    3. Location:
       - Represents a geographical location with x and y coordinates.

    4. Business:
       - Inherits from Node and adds information about a business, including its location, owners, and customers.

    5. Group:
       - Inherits from Node and represents a group of nodes/members.

    6. Organisation:
       - Inherits from Node and represents an organization with a location and members.

    7. SearchResult:
       - A structure to store search results, including an array of nodes and the result size.

    Functions:

    - Node Creation Functions:
      - create_node: Creates a new node.
      - create_individual: Creates a new individual node.
      - create_business: Creates a new business node.
      - create_group: Creates a new group node.
      - create_organisation: Creates a new organization node.

    - Node Modification Functions:
      - add_member: Adds a member to a group or organization.
      - add_owner_or_customer: Adds an owner or customer to a business.

    - Node Deletion Functions:
      - delete_node: Deletes a node and removes its references in the network.
      - remove_node_from_links: Removes a specific node from the links of another node.

    - Node Search Functions:
      - search_node_by_name: Searches for nodes by name.
      - search_node_by_type: Searches for nodes by type.
      - search_individual_by_birthday: Searches for individuals by birthday.

    - Node Link Management Functions:
      - is_node_in_links: Checks if a node is already linked to another node.

    - Content and Display Functions:
      - print_linked_nodes: Prints nodes linked to a specific node.
      - post_content: Posts content to a node.
      - search_and_print_content: Searches and prints content of a specific node.
      - display_linked_content: Displays content linked to a specific node.

    - Utility Functions:
      - print_node_details: Prints details of a specific node.
      - print_all_nodes: Prints details of all nodes in the network.

    - User Interface Function:
      - interface: Implements a user interface for interacting with the social network.

*/

#define MAX_NODES 100 // Set as a default value, can be changed as per requirement

typedef struct Node
{
    int id;
    struct Node **links;
    int num_links;
    char *name;
    char *date; // using the time.h header file to set the date in the format of a string
    char **content;
    int num_contents;
    char type; // I- individual, B- business, G- group, O- organisation
} Node;

extern Node *all_nodes[MAX_NODES];
extern int num_nodes;

typedef struct Individual
{
    Node node;
    char *birthday;
} Individual;

typedef struct Location
{
    double x;
    double y;
} Location;

typedef struct Business
{
    Node node;
    Location location;
    Individual **owners;
    int num_owners;
    Individual **customers;
    int num_customers;
} Business;

typedef struct Group
{
    Node node;
    Node **members;
    int num_members;
} Group;

typedef struct Organisation
{
    Node node;
    Location location;
    Individual *members;
    int num_members;
} Organisation;

typedef struct SearchResult
{
    Node **nodes;
    int size;
} SearchResult;

Node *create_node(char *name, char type);
Individual *create_individual(char *name, char *birthday);
Business *create_business(char *name, Location location);
Group *create_group(char *name);
Organisation *create_organisation(char *name, Location location);

void add_member(Node *group_or_org, Node *new_member);
void add_owner_or_customer(Business *business, Individual *new_owner_or_customer, char role);

void delete_node(char *name);
void remove_node_from_links(Node *node, Node *target);
SearchResult search_node_by_name(char *name);
SearchResult search_node_by_type(char type);
SearchResult search_individual_by_birthday(char *birthday);

int is_node_in_links(Node *node, Node *target);
void print_linked_nodes(char *name);
void post_content(char *name, char *content);
void search_and_print_content(char *name);
void display_linked_content(char *name);

void print_node_details(Node *node);
void print_all_nodes();
void interface();