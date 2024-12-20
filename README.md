"# ProjectI_20241" 

*)PHẦN I: GITHUB

  -Đây là respository để lưu trữ các file code trên hệ thống hustack.
  Các file được push lên github theo workflow như sau :
  
  +)Tôi sẽ tạo 8 branch tương ứng với 8 tuần (Week1,Week2,..Week8) , trong mỗi branch
  tôi tạo những folder tương ứng để chứa file code (week1,week2,..,week8)
  
  +)File code trong mỗi một tuần sẽ được đẩy lên branch tương ứng(ví dụ file arr_queries.cpp
  là bài tập của tuần 1 , sẽ được push lên folder week1 ở trong branch Week1)
  
  +)Sau khi đã push file code của một tuần lên branch tương ứng , tôi sẽ merge branch đó vào
  branch master(default branch)
  
  -Tìm hiểu về cherry-pick:
  
  +)Khái niệm về git cherry-pick:

  git cherry-pick là một lệnh trong Git được sử dụng để áp dụng một hoặc nhiều commit từ một branch này sang branch khác mà không cần phải merge toàn bộ branch.
  
  +)Khi nào sử dụng git cherry-pick
  
•	Khi bạn muốn lấy một số thay đổi cụ thể từ một branch (hoặc commit) mà không cần lấy tất cả các commit hoặc thay đổi từ branch đó.

•	Thường được dùng trong trường hợp bạn cần sửa lỗi (bug fix) hoặc áp dụng một tính năng cụ thể từ branch khác vào branch hiện tại.

  +)Cách hoạt động của git cherry-pick
  
  Lệnh git cherry-pick lấy nội dung của một commit cụ thể từ branch khác và tạo một commit mới với nội dung đó trên branch hiện tại.
  
  +)Cách sử dụng git cherry-pick
  
  1. Cherry-pick một commit duy nhất
  	•	Cú pháp:
  
  git cherry-pick <commit-hash>
  
•	Ví dụ:
  Giả sử bạn đang ở branch main và muốn lấy commit 123abcd từ branch feature:
  git checkout main
  git cherry-pick 123abcd
  
  Commit 123abcd từ branch feature sẽ được áp dụng vào branch main dưới dạng một commit mới.
  
  2. Cherry-pick nhiều commit
  
  Nếu bạn muốn áp dụng một dãy các commit:
  	•	Cú pháp:
  
  git cherry-pick <start-commit>..<end-commit>
  
  
•	Ví dụ:
  Nếu bạn muốn lấy tất cả các commit từ 123abcd đến 789efgh:
  
  git cherry-pick 123abcd..789efgh
  
  3. Cherry-pick với message
  
  Khi cherry-pick, Git sẽ giữ lại thông điệp commit gốc. Nếu muốn thay đổi thông điệp commit, bạn có thể sử dụng:
  
  git cherry-pick -e <commit-hash>
  
  Điều này cho phép bạn chỉnh sửa thông điệp commit trước khi hoàn tất.
  
  4. Hủy bỏ cherry-pick (nếu có lỗi)
  
  Nếu bạn cherry-pick nhưng có lỗi hoặc muốn hủy bỏ, bạn có thể:
  •	Hủy cherry-pick đang thực hiện:
  
  git cherry-pick --abort
  
  
  •	Hủy commit cherry-pick đã áp dụng:
  
  git reset --hard HEAD~1
  
  +)Ưu điểm của git cherry-pick
  
  •	Linh hoạt: Cho phép áp dụng các commit cụ thể mà không cần merge toàn bộ branch.
  •	Kiểm soát tốt hơn: Giúp bạn chọn lọc thay đổi mà bạn thực sự cần.
  
 +)Hạn chế của git cherry-pick
  
  •	Có thể làm phức tạp lịch sử Git nếu sử dụng quá nhiều.
  •	Không nên sử dụng thường xuyên trong các dự án lớn với nhiều người vì có thể dẫn đến xung đột hoặc commit trùng lặp.
  
  +)Ví dụ thực tế
  
  •	Sửa lỗi (bug fix): Lấy commit sửa lỗi từ branch develop và áp dụng vào branch hotfix.
  •	Cập nhật tính năng: Lấy commit từ branch feature để tích hợp một tính năng vào branch main.
  -)Tìm hiểu về Release trong Github:
    Tính năng Release trên GitHub cho phép bạn đóng gói và phân phối các phiên bản cụ thể của dự án đến người dùng. Mỗi bản phát hành (release) thường đi kèm với các thông tin như ghi chú phát hành, tài sản đính kèm (như tệp nhị phân hoặc tài liệu), và liên     kết đến mã nguồn tại thời điểm phát hành.
  
  +Mục đích của Release trên GitHub
  
  •	Đánh dấu phiên bản ổn định: Giúp người dùng dễ dàng truy cập và sử dụng phiên bản ổn định của dự án.
  •	Cung cấp thông tin chi tiết: Ghi chú phát hành cung cấp thông tin về các tính năng mới, sửa lỗi và cải tiến trong phiên bản đó.
  •	Phân phối tệp đính kèm: Cho phép đính kèm các tệp như tệp cài đặt, tài liệu hướng dẫn hoặc các tài nguyên liên quan khác.
  
  +Cách tạo Release trên GitHub
  
  1.	Truy cập repository của bạn trên GitHub.
  2.	Chọn tab “Releases” ở phía trên của trang repository.
  3.	Nhấp vào “Draft a new release”.
  4.	Điền thông tin:
  •	Tag version: Đặt tên phiên bản (ví dụ: v1.0.0).
  •	Target branch: Chọn nhánh chứa mã nguồn cho phiên bản này.
  •	Release title: Tiêu đề cho bản phát hành.
  •	Release description: Ghi chú chi tiết về các thay đổi, tính năng mới hoặc sửa lỗi.
  5.	Đính kèm tệp (nếu cần): Kéo và thả các tệp vào khu vực đính kèm để bổ sung tài nguyên cho bản phát hành.
  6.	Chọn “This is a pre-release” nếu đây là phiên bản thử nghiệm chưa ổn định.
  7.	Nhấp vào “Publish release” để công bố bản phát hành.
  
  Lưu ý: Chỉ những người có quyền push lên repository mới có thể tạo release. ￼
  
  +Lợi ích của việc sử dụng Release trên GitHub
  
  •	Quản lý phiên bản hiệu quả: Dễ dàng theo dõi và quản lý các phiên bản khác nhau của dự án.
  •	Cung cấp thông tin rõ ràng: Người dùng và cộng tác viên có thể nhanh chóng nắm bắt các thay đổi và cập nhật trong từng phiên bản.
  •	Phân phối tài nguyên thuận tiện: Cho phép người dùng tải về các tệp liên quan trực tiếp từ trang release.
  -)Tính năng về Page trong Github:
    GitHub Pages là một dịch vụ miễn phí do GitHub cung cấp, cho phép bạn lưu trữ và xuất bản các trang web tĩnh trực tiếp từ kho lưu trữ (repository) trên GitHub. Dịch vụ này thường được sử dụng để tạo trang cá nhân, blog, tài liệu dự án hoặc trang giới        thiệu cho các dự án mã nguồn mở.
    
+)Lợi ích của GitHub Pages
    
  •	Miễn phí và dễ sử dụng: Bạn có thể triển khai trang web mà không cần chi phí lưu trữ hoặc tên miền.
  •	Tích hợp với GitHub: Dễ dàng quản lý và cập nhật nội dung thông qua hệ thống kiểm soát phiên bản của Git.
  •	Hỗ trợ Jekyll: Cho phép sử dụng Jekyll để tạo và quản lý trang web tĩnh một cách hiệu quả.
  
    +)Cách tạo và triển khai trang web với GitHub Pages
    
1.	Tạo một kho lưu trữ mới trên GitHub:
•	Đăng nhập vào tài khoản GitHub của bạn.
•	Nhấp vào nút “New” để tạo repository mới.
•	Đặt tên cho repository theo định dạng username.github.io (thay username bằng tên người dùng GitHub của bạn).
2.	Thêm nội dung cho trang web:
•	Clone repository về máy tính của bạn:
  
  git clone https://github.com/username/username.github.io
  

•	Thêm các tệp HTML, CSS, JavaScript hoặc sử dụng Jekyll để tạo nội dung.
•	Commit và push các thay đổi lên GitHub:
  
  git add .
  git commit -m "Initial commit"
  git push origin main
  
  
3.	Cấu hình GitHub Pages:
•	Truy cập vào phần “Settings” của repository.
•	Cuộn xuống phần “GitHub Pages”.
•	Trong mục “Source”, chọn nhánh (main hoặc gh-pages) và thư mục gốc (/root) để triển khai trang web.
•	Nhấp vào “Save” để lưu cấu hình.
4.	Truy cập trang web:
•	Sau khi cấu hình, trang web của bạn sẽ được xuất bản tại địa chỉ https://username.github.io.
  
  +)Tùy chỉnh nâng cao

•	Sử dụng tên miền tùy chỉnh: Bạn có thể cấu hình để sử dụng tên miền riêng bằng cách thêm tệp CNAME chứa tên miền vào repository và cấu hình DNS trỏ về GitHub Pages.
•	Bảo mật với HTTPS: GitHub Pages hỗ trợ HTTPS, giúp bảo mật kết nối cho trang web của bạn.


    
          
