"""
Link : https://refactoring.guru/design-patterns/chain-of-responsibility (Example-1)
Link : https://www.geeksforgeeks.org/system-design/chain-responsibility-design-pattern/

-> Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon
receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

> Chain of Responsibility (CoR) নীতি হলো একটি behavioral design pattern যা একটি রিকোয়েস্ট বা অনুরোধের প্রক্রিয়াকরণ একাধিক হ্যান্ডলারের
মধ্যে শৃঙ্খলাবদ্ধভাবে (chain) বিতরণ করে। নীতিটির মূল ধারণা হলো:

1. রিসিভার ও হ্যান্ডলার আলাদা করা:
প্রতিটি হ্যান্ডলার স্বতন্ত্র অবজেক্ট হিসেবে থাকে এবং সিদ্ধান্ত নেয় যে সে রিকোয়েস্টটি প্রক্রিয়া করতে পারবে কি না।

2. চেইন তৈরি করা:
যদি বর্তমান হ্যান্ডলার রিকোয়েস্টটি প্রক্রিয়া করতে না পারে, তবে রিকোয়েস্টটি পরবর্তী হ্যান্ডলারের কাছে পাঠানো হয়।

3. ডিকাপলিং (Decoupling):
ক্লায়েন্ট রিকোয়েস্ট পাঠায় কিন্তু জানে না কোন হ্যান্ডলার এটি প্রক্রিয়া করবে। হ্যান্ডলারগুলোর মধ্যে সম্পর্ক চেইন অনুযায়ী তৈরি হয়।

4. ফ্লেক্সিবিলিটি:
নতুন হ্যান্ডলার যোগ বা চেইনের ক্রম পরিবর্তন সহজ, কারণ হ্যান্ডলারগুলো স্বতন্ত্র এবং পরবর্তী হ্যান্ডলারকে শুধু execute বা সমতুল্য মেথডের মাধ্যমে জানে।


> The Chain of Responsibility design pattern has a few key elements that work together to pass a request along a chain
until it’s handled.

1. Handler (Abstract Interface or Base Class)
    * Defines a common interface for handling requests.
    * Usually includes:
        * handle(request) method to process the request.
        * A reference to the next handler in the chain.
    * Often includes a method like set_next(handler) to link handlers together.

Purpose: Ensures all handlers share the same contract, so they can be linked in a chain.

2. Concrete Handlers
    * Classes that implement the Handler interface.
    * Each one decides:
        * Whether to handle the request.
        * Or pass it to the next handler in the chain.
    * Each can handle specific conditions.

Purpose: Encapsulate different processing logic at each stage in the chain.

3. Client
    * Creates the chain of handlers.
    * Sends the request to the first handler in the chain.
    * Doesn’t care who in the chain handles it — just starts the process.

Purpose: Decouples request sender from request processing logic.

4. Request (Optional in Some Implementations)
    * The object containing the data to be processed.
    * Can be as simple as a primitive (string, int) or a full object with multiple attributes.

Purpose: Allows passing structured data along the chain.

# Simple Visual Flow
Client → Handler1 → Handler2 → Handler3 → (Handled or Dropped)
"""

from abc import ABC, abstractmethod
from enum import Enum

class Complexity(Enum):
    Simple = "SIMPLE"
    Moderate = "MODERATE"
    Complex = "COMPLEX"

# Ticket Class
class SupportTicket:
    def __init__(self, ticket_id: str, complexity: Complexity, description: str):
        self._ticket_id = ticket_id
        self._complexity = complexity
        self._description = description

    @property
    def get_complexity(self):
        return self._complexity

    @property
    def get_ticket_id(self):
        return self._ticket_id

    @property
    def get_description(self):
        return self._description

# Handler Interface
class SupportTeam(ABC):
    @abstractmethod
    def set_next_team(self, next_team: 'SupportTeam'):
        pass

    @abstractmethod
    def handle_ticket(self, ticket: SupportTicket):
        pass

# Concrete Handlers
class HelpDeskTeam(SupportTeam):
    def __init__(self):
        self._next_team = None

    def set_next_team(self, next_team: SupportTeam):
        self._next_team = next_team

    def handle_ticket(self, ticket: SupportTicket):
        if ticket.get_complexity == Complexity.Simple:
            print(f"Help Desk Team resolved ticket {ticket.get_ticket_id}: {ticket.get_description}")
        elif self._next_team is not None:
            print(f"Help Desk Team escalating ticket {ticket.get_ticket_id} to next team.")
            self._next_team.handle_ticket(ticket)


class TechnicalSupportTeam(SupportTeam):
    def __init__(self):
        self._next_team = None

    def set_next_team(self, next_team: SupportTeam):
        self._next_team = next_team

    def handle_ticket(self, ticket: SupportTicket):
        if ticket.get_complexity == Complexity.Moderate:
            print(f"Technical Support Team resolved ticket {ticket.get_ticket_id}: {ticket.get_description}")
        elif self._next_team is not None:
            print(f"Technical Support Team escalating ticket {ticket.get_ticket_id} to next team.")
            self._next_team.handle_ticket(ticket)


class EngineeringTeam(SupportTeam):
    def set_next_team(self, next_team: SupportTeam):
        pass

    def handle_ticket(self, ticket: SupportTicket):
        if ticket.get_complexity == Complexity.Complex:
            print(f"Engineering Team resolved ticket {ticket.get_ticket_id}: {ticket.get_description}")
        else:
            print(f"Ticket {ticket.get_ticket_id} cannot be resolved by any team: {ticket.get_description}")

if __name__ == "__main__":
    help_desk = HelpDeskTeam()
    tech_support = TechnicalSupportTeam()
    engineering = EngineeringTeam()

    help_desk.set_next_team(tech_support)
    tech_support.set_next_team(engineering)

    ticket1 = SupportTicket("TICKET-001", Complexity.Simple, "Reset Password for user account.")
    ticket2 = SupportTicket("TICKET-002", Complexity.Moderate, "Troubleshoot network connectivity issue")
    ticket3 = SupportTicket("TICKET-003", Complexity.Complex, "Fix critical database corruption")
    ticket4 = SupportTicket("TICKET-004", Complexity.Simple, "Update user email address")

    help_desk.handle_ticket(ticket1)
    help_desk.handle_ticket(ticket2)
    help_desk.handle_ticket(ticket3)
    help_desk.handle_ticket(ticket4)

