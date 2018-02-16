from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def test_phrase1(self):
        self.client.get("/test1")

    @task(1)
    def test_phrase2(self):
        self.client.get("/test2")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
