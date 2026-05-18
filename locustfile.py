from locust import HttpUser, between, task

class MiPrueba(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def homepage(self):
        # CAMBIA esta URL por la de TU sitio web
        self.client.get("https://xat.com/foros019")
