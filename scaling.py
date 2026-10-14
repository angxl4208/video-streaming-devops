"""Auto-scaling logic for a video streaming platform."""


def required_servers(viewers, viewers_per_server=100):
    if viewers < 0 or viewers_per_server <= 0:
        raise ValueError("Invalid input")

    servers = (viewers + viewers_per_server - 1) // viewers_per_server
    return max(1, servers)


def average_load(viewers, servers):
    if viewers < 0 or servers <= 0:
        raise ValueError("Invalid input")

    return viewers / servers