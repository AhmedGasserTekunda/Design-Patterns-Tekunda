# observer_pattern/observer.py
class NewsPublisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, news):
        for subscriber in self._subscribers:
            subscriber.update(news)


class EmailSubscriber:
    def __init__(self, email):
        self.email = email

    def update(self, news):
        print(f"Email to {self.email}: {news}")


if __name__ == "__main__":
    publisher = NewsPublisher()

    alice = EmailSubscriber("alice@example.com")
    bob = EmailSubscriber("bob@example.com")

    publisher.subscribe(alice)
    publisher.subscribe(bob)

    publisher.notify_subscribers("New article published: Observer Pattern in Python")