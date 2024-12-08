#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <sstream>
#include <iterator>

using namespace std;

class Company {
private:
    int total_orders = 0;  // Tong so don hang
    int total_revenue = 0; // Tong doanh thu
    unordered_map<string, int> revenue_of_shop;  // Doanh thu cua cac cua hang
    unordered_map<string, unordered_map<string, int>> customer_buy;  // Chi tieu cua khach hang tai cua hang
    map<string, int> timepoint_price;  // Doanh thu theo thoi gian, sap xep theo thoi gian
    vector<int> prefix_sum;  // Tong doanh thu tich luy
    vector<string> sorted_timepoints;  // Thoi gian da sap xep

public:
    Company(const vector<string>& orders) {
        // Xu ly moi don hang va cap nhat thong tin
        for (const string& order : orders) {
            istringstream iss(order);
            vector<string> lst{istream_iterator<string>{iss}, istream_iterator<string>{}};
            string customer_id = lst[0];
            string product_id = lst[1];
            int price = stoi(lst[2]);
            string shop_id = lst[3];
            string timepoint = lst[4];

            // Cap nhat tong so don hang va doanh thu
            total_orders++;
            total_revenue += price;

            // Cap nhat doanh thu cua cua hang
            revenue_of_shop[shop_id] += price;

            // Cap nhat chi tieu cua khach hang tai cua hang
            customer_buy[customer_id][shop_id] += price;

            // Cap nhat doanh thu theo thoi gian
            timepoint_price[timepoint] += price;
        }

        // Sap xep thoi gian va tinh toan tong doanh thu tich luy
        for (const auto& [time, revenue] : timepoint_price) {
            sorted_timepoints.push_back(time);
            if (prefix_sum.empty())
                prefix_sum.push_back(revenue);
            else
                prefix_sum.push_back(prefix_sum.back() + revenue);
        }
    }

    // Tra ve tong so don hang
    int total_number_orders() const {
        return total_orders;
    }

    // Tra ve tong doanh thu
    int get_total_revenue() const {
        return total_revenue;
    }

    // Tra ve doanh thu cua cua hang theo id
    int get_revenue_of_shop(const string& shop_id) const {
        auto it = revenue_of_shop.find(shop_id);
        return (it != revenue_of_shop.end()) ? it->second : 0;
    }

    // Tra ve tong chi tieu cua khach hang tai cua hang
    int total_consume_of_customer_shop(const string& customer_id, const string& shop_id) const {
        auto customer_it = customer_buy.find(customer_id);
        if (customer_it != customer_buy.end()) {
            auto shop_it = customer_it->second.find(shop_id);
            return (shop_it != customer_it->second.end()) ? shop_it->second : 0;
        }
        return 0;
    }

    // Tra ve tong doanh thu trong khoang thoi gian
    int total_revenue_in_period(const string& from_time, const string& to_time) const {
        // Tim vi tri bat dau va ket thuc cua khoang thoi gian
        auto start_it = lower_bound(sorted_timepoints.begin(), sorted_timepoints.end(), from_time);
        auto end_it = upper_bound(sorted_timepoints.begin(), sorted_timepoints.end(), to_time);

        if (start_it == sorted_timepoints.end() || start_it > end_it)
            return 0;

        int start_index = distance(sorted_timepoints.begin(), start_it);
        int end_index = distance(sorted_timepoints.begin(), end_it) - 1;

        // Tinh tong doanh thu trong khoang thoi gian
        int total = prefix_sum[end_index];
        if (start_index > 0) {
            total -= prefix_sum[start_index - 1];
        }
        return total;
    }
};

int main() {
    vector<string> orders;
    string line;

    // Doc don hang cho den khi gap '#'
    while (getline(cin, line)) {
        if (line == "#") break;
        orders.push_back(line);
    }

    // Khoi tao class Company voi danh sach don hang
    Company company(orders);

    // Xu ly cac truy van
    while (getline(cin, line)) {
        if (line == "#") break;

        if (line == "?total_number_orders") {
            cout << company.total_number_orders() << endl;  // In tong so don hang
        } else if (line == "?total_revenue") {
            cout << company.get_total_revenue() << endl;  // In tong doanh thu
        } else {
            istringstream iss(line);
            vector<string> lst{istream_iterator<string>{iss}, istream_iterator<string>{}};
            if (lst[0] == "?revenue_of_shop") {
                cout << company.get_revenue_of_shop(lst[1]) << endl;  // In doanh thu cua cua hang
            } else if (lst[0] == "?total_consume_of_customer_shop") {
                cout << company.total_consume_of_customer_shop(lst[1], lst[2]) << endl;  // In chi tieu cua khach hang tai cua hang
            } else if (lst[0] == "?total_revenue_in_period") {
                cout << company.total_revenue_in_period(lst[1], lst[2]) << endl;  // In doanh thu trong khoang thoi gian
            }
        }
    }

    return 0;
}

