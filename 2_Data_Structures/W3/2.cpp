#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Job
{
private:
    long long num_workers;
    vector<long long> jobs;
    vector<long long> assigned_workers;
    vector<long long> start_times;

    void WriteResponse() const
    {
        for (int i = 0; i < jobs.size(); i++)
        {
            cout << assigned_workers[i] << " " << start_times[i] << endl;
        }
    }

    void ReadData()
    {
        long long m;
        cin >> num_workers >> m;
        jobs.resize(m);
        for (int i = 0; i < m; i++)
        {
            cin >> jobs[i];
        }
    }

    void AssignJobs()
    {
        assigned_workers.resize(jobs.size());
        start_times.resize(jobs.size());
        vector<long long> next_free_time(num_workers, 0);

        long long next_worker = 0;

        for (int i = 0; i < jobs.size(); i++)
        {
            long long duration = jobs[i];
            assigned_workers[i] = next_worker;
            start_times[i] = next_free_time[next_worker];
            next_free_time[next_worker] += duration;
            next_worker += 1;
            if (next_worker >= num_workers)
            {
                next_worker = 0;
            }
        }
    }

public:
    void Solve()
    {
        ReadData();
        AssignJobs();
        WriteResponse();
    }
};

int main()
{
    Job j;
    j.Solve();
    return 0;
}