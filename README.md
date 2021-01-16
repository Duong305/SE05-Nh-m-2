# SE05-Nhom2 (AutoCad với Python)
Với đề tài này bọn em đã biết được thêm về các thuật toán là xoay hình 3d và dùng phương trình bezier để vẽ đường cong bằng cách nối đoạn thẳng từ nhiều đoạn thẳng
* File allViews.py là để vẽ ra các tấm gỗ hay dc gọi là các thành phần của tủ các tấm đó từ cái tủ dc tách ra thành nhiều tấm cách nhau 1 khoảng nhất định và chú thích tên của từng tấm vào đúng vị trí của tấm đó
  + Đầu tiên bọn em sẽ lấy các dữ liệu được lấy từ file xml là các toạ độ điểm, chiều dài, chiều rộng, chiều cao góc xoay quanh trục 
  + Tiếp theo bọn em sẽ tạo ra 1 list chứa toạ độ điểm của mỗi tấm, 1 list chứa chiều dài, chiều rộng, chiều cao của mỗi tấm, 1 list chứa tên của mỗi tấm rồi tịnh tiến các tấm       thành phần của tủ đó bằng cách thêm bớt các giá trị x, các giá trị y vì ở đây bọn em giữ nguyên vị trí 3 tấm ở giữa của toạ độ và thêm tên vào mỗi tấm đó
  + Cuối cùng bọn em sẽ vẽ các tấm đó bằng cách nối đoạn thẳng giữa 2 điểm với điều kiện là áp dụng công thức toán bọn em sẽ tính được khoảng cách nhờ toạ độ điểm của các tấm nếu   khoảng cách đó bằng chiều dài, chiều rộng, chiều cao của tấm thì thực hiện việc vẽ
  
* File bezierAlgo sử dụng thuật toán hay phương trình đường cong bezier để vẽ ra các đường cong từ việc nối rất nhiều đoạn thẳng cực nhỏ giữa các đoạn thẳng đó có độ chênh lệch nghiêng cực nhỏ tức phương trình trên biến các điểm điều khiển đường cong thành nhiều điểm cực sát nhau có quỹ đạo trở thành đường cong rồi nối trúng lại với nhau bhằng phương thức add_line() của ezdxf là phương thức nối đoạn thẳng giữa 2 điểm
