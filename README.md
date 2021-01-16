# SE05-Nhom2 (AutoCad với Python)
Với đề tài này bọn em đã biết được thêm về các thuật toán là xoay hình 3d và dùng phương trình bezier để vẽ đường cong bằng cách nối đoạn thẳng từ nhiều đoạn thẳng
* File allViews.py là để vẽ ra các tấm gỗ hay dc gọi là các thành phần của tủ các tấm đó từ cái tủ dc tách ra thành nhiều tấm cách nhau 1 khoảng nhất định và chú thích tên của từng tấm vào đúng vị trí của tấm đó
  + Đầu tiên bọn em sẽ lấy các dữ liệu được lấy từ file xml là các toạ độ điểm, chiều dài, chiều rộng, chiều cao, tên của mỗi tấm.  
  + Tiếp theo bọn em sẽ tạo ra 1 list chứa toạ độ điểm của mỗi tấm, 1 list chứa chiều dài, chiều rộng, chiều cao của mỗi tấm, 1 list chứa tên của mỗi tấm rồi tịnh tiến các tấm       thành phần của tủ đó bằng cách thêm bớt các giá trị x, các giá trị y của toạ độ điểm vì ở đây bọn em giữ nguyên vị trí 3 tấm ở giữa rồi sau đó lưu lại các giá trị x,y thay đổi đó vào list rỗng khác và thêm tên vào mỗi tấm đó.
  + Nhờ list lưu lại các giá trị x,y,z đã thay đổi trên bọn em sẽ vẽ các tấm đó bằng cách nối đoạn thẳng giữa 2 điểm với điều kiện là áp dụng công thức toán bọn em sẽ tính được khoảng cách nhờ toạ độ điểm của các tấm nếu khoảng cách đó bằng chiều dài, chiều rộng, chiều cao của tấm thì thực hiện việc vẽ.

* File XoayCacTam.py là để xoay các tấm đó quanh các trục x,y,z sử dụng thuật toán xoay hình 3d liên quan đến lượng giác
  + Đầu tiên bọn cũng em sẽ lấy các dữ liệu được lấy từ file xml là các toạ độ điểm, chiều dài, chiều rộng, chiều cao, tên của mỗi tấm, góc xoay quanh trục của mỗi tấm
  + Tiếp theo bọn em cũng sẽ tạo ra 1 list chứa toạ độ điểm của mỗi tấm, 1 list chứa chiều dài, chiều rộng, chiều cao của mỗi tấm, 1 list chứa các góc xoay quanh trục của mỗi tấm, rồi bằng thuật toán xoay hình 3d bọn em sẽ thay đổi các giá trị x, các giá trị y, các giá trị z của tọa độ điểm mỗi tấm. Sau đó bọn em lưu hết các giá trị x, y, z đó vào 1 list rỗng khác.
  + Nhờ list lưu lại các giá trị x,y,z đã thay đổi trên bọn em sẽ vẽ các tấm đó bằng cách nối đoạn thẳng giữa 2 điểm với điều kiện là áp dụng công thức toán bọn em sẽ tính được khoảng cách nhờ toạ độ điểm của các tấm nếu khoảng cách đó bằng chiều dài, chiều rộng, chiều cao của tấm thì thực hiện việc vẽ vì sau khi xoay tấm quanh các trục thì các kích thứơc ban đầu sẽ thay đổi nhưng mỗi tấm sau khi xoay sẽ vẫn có 3 kích thước ban đầu đó ở đầu vào ví dụ sau khi xoay chiều dài sẽ biến thành chiều rộng và ngược lại. 

* File bezierAlgo sử dụng thuật toán hay phương trình đường cong bezier để vẽ ra các đường cong từ việc nối rất nhiều đoạn thẳng cực nhỏ giữa các đoạn thẳng đó có độ chênh lệch nghiêng cực nhỏ tức phương trình trên biến các điểm điều khiển đường cong thành nhiều điểm cực sát nhau có quỹ đạo trở thành đường cong rồi nối trúng lại với nhau bhằng phương thức add_line() của ezdxf là phương thức nối đoạn thẳng giữa 2 điểm
  + Đầu tiên bọn em lấy dữ liệu từ file svg là các tọa độ điểm của các điểm điều khiển đường cong
  + Tiếp theo bọn em sẽ tạo ra list d để chứa các list chứa các toạ độ điểm của từng đường cong tức mỗi list trong list d đó chứa các toạ độ điểm của 1 đường cong rồi sau đó tạo thêm list a để chứa các list rỗng trong mỗi list rỗng đó sẽ được thêm vào các bộ toạ độ điểm mà bọn em đã tính được là giá trị x, giá trị y nhờ áp dụng phương trình đường cong bezier biến các điểm điều khiển đường cong thành nhiều điểm cực sát nhau có quỹ đạo trở thành đường cong
  + Nhờ list a ở trên bọn em sẽ thực hiện vẽ các đường cong nhờ phương thức add_line() của ezdxf là phương thức nối đoạn thẳng giữa 2 điểm
