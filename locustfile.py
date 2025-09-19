from locust import HttpUser, task


class Usuario(HttpUser):
    @task
    def index(self):
        self.client.get("https://example.com")
