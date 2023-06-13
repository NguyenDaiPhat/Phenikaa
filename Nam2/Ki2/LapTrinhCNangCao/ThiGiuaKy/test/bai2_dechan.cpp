#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;
// cau 1
struct Movie
{
    int rank;
    string name;
    int year;
    double rating;
    vector<string> genre;
    string certificate;
    double run_time;
    long long budger;
    long long box_office;
    vector<string> casts;
    vector<string> directors;
    vector<string> writers;
};
// cau 3
vector<Movie> xulyPath(string path)
{
    ifstream input;
    input.open(path);
    if (!input.is_open())
    {
        cout << " can not to open file ";
        exit(0);
    }
    string s, line;
    vector<Movie> movies;
    getline(input, line);
    while (getline(input, line))
    {
        Movie movie;
        stringstream iss(line);
        string token;

        // rank
        getline(iss, token, ',');
        movie.rank = stoi(token);

        // name
        getline(iss, token, ',');
        movie.name = token;

        // year
        getline(iss, token, ',');
        movie.year = stoi(token);

        // rating
        getline(iss, token, ',');
        movie.rating = stod(token);

        // genre
        getline(iss, token, ',');
        stringstream genreStream(token);
        while (getline(genreStream, token, ';'))
        {
            movie.genre.push_back(token);
        }

        // certificate
        getline(iss, token, ',');
        movie.certificate = token;

        // run_time
        getline(iss, token, ',');
        stringstream runtimeStream(token);
        double hours, minutes;
        char delimiter;
        runtimeStream >> hours >> delimiter >> minutes;
        movie.run_time = hours * 60 + minutes;

        // budger
        getline(iss, token, ',');
        movie.budger = stoll(token);

        // box_office
        getline(iss, token, ',');
        movie.box_office = stoll(token);

        // casts
        getline(iss, token, ',');
        stringstream castsStream(token);
        while (getline(castsStream, token, ';'))
        {
            movie.casts.push_back(token);
        }

        // directors
        getline(iss, token, ',');
        stringstream directorsStream(token);
        while (getline(directorsStream, token, ';'))
        {
            movie.directors.push_back(token);
        }

        // writers
        getline(iss, token, ',');
        stringstream writersStream(token);
        while (getline(writersStream, token, ';'))
        {
            movie.writers.push_back(token);
        }

        movies.push_back(movie);
    }
    return movies;
}

// cau4
void cau4(vector<Movie> movie, string directorName)
{
    cout << "Cac bo phim duoc chi dao boi " << directorName << "la: ";
    long long tong = 0;
    for (auto i : movie)
    {
        for (auto j : i.directors)
            if (j == directorName)
            {
                tong += i.box_office;
                cout << i.name << " ";
            }
    }
    cout << endl
         << "Tong doanh thu cac phim duoc " << directorName << " chi dao la: " << tong;
    cout << endl;
}

// cau 5
int count(vector<Movie> movie, string run_time)
{
    int count1 = 0;
    istringstream iss(run_time);
    char tam;
    double h, p, thoigian;
    iss >> h >> tam >> p;
    thoigian = h * 60 + p;
    for (auto i : movie)
        if (i.run_time >= thoigian)
        {
            count1++;
        }
    // cout<<"So luong phim co do dai lon hon hoac bang run_time la: "<< count1;
    return count1;
}

// cau6
void cau6(vector<Movie> movie, string actName)
{
    ofstream output;
    output.open("output.txt");
    if (!output.is_open())
    {
        cout << "can not open file output.txt";
    }
    for (auto i : movie)
        for (auto j : i.casts)
        {
            if (j == actName)
                output << i.name << endl;
        }
    output.close();
}

int main(int argc, char *argv[])
{
    // cau 2
    string path, directorName, actName, run_time;
    for (int i = 0; i < argc; i++)
    {
        if (string(argv[i]) == string("-p"))
            path = argv[i + 1];
        else if (string(argv[i]) == string("-d"))
            directorName = argv[i + 1];
        else if (string(argv[i]) == string("-a"))
            actName = argv[i + 1];
        else if (string(argv[i]) == string("-r"))
            run_time = argv[i + 1];
    }
    // cau 3
    vector<Movie> movies = xulyPath(path);
    // cau 4
    cau4(movies, directorName);
    // cau 5
    int dem = count(movies, run_time);
    cout << "So luong bo phim co do dai lon hon hoac bang " << run_time << " la: " << dem << endl;
    // cau6
    cau6(movies, actName);
    // for (auto i : movies)
    // {
    //     cout << i.rank << endl;
    //     cout << i.name << endl;
    //     cout << i.year << endl;
    //     cout << i.rating << endl;
    //     for (auto j : i.genre)
    //     {
    //         cout << j << endl;
    //     }
    //     cout << i.certificate << endl;
    //     cout << i.run_time << endl;
    //     cout << i.budger << endl;
    //     cout << i.box_office << endl;
    //     for (auto j : i.casts)
    //     {
    //         cout << j << endl;
    //     }
    //     for (auto j : i.directors)
    //     {
    //         cout << j << endl;
    //     }
    //     for (auto j : i.writers)
    //     {
    //         cout << j << endl;
    //     }
    //     cout << endl;
    // }

    return 0;
}