
from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.next_finish_time = 0
        self.finish_time = []
        self.bufferspace = 0
        self.result = []

    def process(self, request):
        if self.bufferspace == 0:
            self.bufferspace += 1
            self.next_finish_time += request.time_to_process
            self.result.append(Response(False, request.arrived_at))
            self.finish_time.append(self.next_finish_time)

        elif request.arrived_at < self.next_finish_time and self.bufferspace < self.size:
            self.bufferspace += 1
            self.result.append(Response(False, self.next_finish_time))
            self.next_finish_time += request.time_to_process
            self.finish_time.append(self.next_finish_time)

        elif request.arrived_at >= self.next_finish_time:
            self.bufferspace = 0
            self.result.append(Response(False, request.arrived_at))
            self.next_finish_time += request.time_to_process
            self.finish_time.append(self.next_finish_time)

        elif request.arrived_at < self.next_finish_time and self.bufferspace >= self.size:
            while self.finish_time[0] <= request.arrived_at:
                self.bufferspace -= 1
                del self.finish_time[0]

            if self.bufferspace < self.size:
                self.bufferspace += 1
                self.result.append(Response(False, self.next_finish_time))
                self.next_finish_time += request.time_to_process
                self.finish_time.append(self.next_finish_time)

            else:
                self.result.append(Response(True, -1))

    def return_the_solution(self):
        return self.result


def process_requests(requests, buffer):

    for request in requests:
        buffer.process(request)

    result = buffer.return_the_solution()

    return result


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
