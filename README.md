# SE05-Nhom2 (AutoCad thử nghiệm thuật toán biến đổi hình học với Python)
Cad là để vẽ các bản vẽ phục vụ cho việc xây dựng và sản xuất. Với đề tài này chúng mình đã biết được thêm về thuật toán là xoay hình 3d và dùng phương trình bezier để vẽ đường cong bằng cách nối nhiều đoạn thẳng rất nhỏ lại với nhau

Những người đóng góp:
  * Hồ Sĩ Dương - 18001029 - K63A5 - HUS  
  * Phạm Trí Đức - 18001032 - K63A5 - HUS
  
Yêu cầu:
  * Ít nhất phải là python 3.6, cài đặt thêm các thư viện ezdxf 0.14.2, more_itertools của python
    + Hướng dẫn cài đặt(đối với hệ điều hành Windows): 
      + Trước tiên bạn phải cập nhật pip gõ lệnh trên Command Prompt 
      ``` python -m pip install --upgrade pip ```
      + Sau đó gõ lệnh 
       ``` pip install ezdxf ``` 
       ``` pip install more_itertools ```
       
Tài liệu tham khảo:
  * [Xoay hình 3D](https://www.it-swarm-vi.tech/vi/math/xoay-mot-vector-trong-khong-gian-3d/1071293716/)
  * [Đường cong bezier](https://vi.wikipedia.org/wiki/%C4%90%C6%B0%E1%BB%9Dng_cong_B%C3%A9zier)
  
Trước khi thực hiện việc vẽ chúng mình sẽ hướng dẫn các bạn sử dụng các lệnh để từ ezdxf xuất ra file dxf và cách lấy dữ liệu từ file xml hoặc svg:
  * ví dụ về việc xuất ra file dxf:
    ``` import ezdxf
        doc = ezdxf.new('R2010')
        ........
        doc.saveas('filename.dxf') 
    ```
  * ví dụ về việc lấy dữ liệu của file xml hoặc svg:
    ``` import xml.dom.minidom 
        doc = xml.dom.minidom.parse("allView_data.xml") # đối với file allView_data.xml
        expertise = doc.getElementsByTagName("globalP")
        for i in expertise:
          x = i.getAttribute("x")
          y = i.getAttribute("y")
          z = i.getAttribute("z") # Đối với file svg cũng làm tương tự nhưng bạn nhớ đổi dạng file truyền vào xml.dom.minidom.parse("filename.svg") 
    ```
Thực hiện việc vẽ hoặc xoay hình bằng các thuật toán:          
  * File allViews.py là để vẽ ra các tấm gỗ hay dc gọi là các thành phần của tủ các tấm đó từ cái tủ dc tách ra thành nhiều tấm cách nhau 1 khoảng nhất định và chú thích tên của     từng tấm vào đúng vị trí của tấm đó
    + Đầu tiên chúng mình sẽ lấy các dữ liệu được lấy từ file xml là các toạ độ điểm, chiều dài, chiều rộng, chiều cao, tên của mỗi tấm.  
    + Tiếp theo chúng mình sẽ tạo ra 1 list chứa toạ độ điểm của mỗi tấm, 1 list chứa chiều dài, chiều rộng, chiều cao của mỗi tấm, 1 list chứa tên của mỗi tấm rồi tịnh tiến các       tấm thành phần của tủ đó bằng cách thêm bớt các giá trị x, các giá trị y của toạ độ điểm vì ở đây chúng mình giữ nguyên vị trí 3 tấm ở giữa rồi sau đó lưu lại các giá trị       x,y thay đổi đó vào list rỗng khác và thêm tên vào mỗi tấm đó.
    + Nhờ list lưu lại các giá trị x,y,z đã thay đổi trên chúng mình sẽ vẽ các tấm đó bằng cách nối đoạn thẳng giữa 2 điểm với điều kiện là áp dụng công thức toán chúng mình sẽ       tính được khoảng cách nhờ toạ độ điểm của các tấm nếu khoảng cách đó bằng chiều dài, chiều rộng, chiều cao của tấm thì thực hiện việc vẽ.

  * File XoayCacTam.py là để xoay các tấm đó quanh các trục x,y,z sử dụng thuật toán xoay hình 3d liên quan đến lượng giác
    + Đầu tiên chúng mình cũng sẽ lấy các dữ liệu được lấy từ file xml là các toạ độ điểm, chiều dài, chiều rộng, chiều cao, tên của mỗi tấm, góc xoay quanh trục của mỗi tấm
    + Tiếp theo chúng mình cũng sẽ tạo ra 1 list chứa toạ độ điểm của mỗi tấm, 1 list chứa chiều dài, chiều rộng, chiều cao của mỗi tấm, 1 list chứa các góc xoay quanh trục của       mỗi tấm, rồi bằng thuật toán xoay hình 3d chúng mình sẽ thay đổi các giá trị x, các giá trị y, các giá trị z của tọa độ điểm mỗi tấm. Sau đó chúng mình lưu hết các giá trị       x, y, z đó vào 1 list rỗng khác.
    + Nhờ list lưu lại các giá trị x,y,z đã thay đổi trên chúng mình sẽ vẽ các tấm đó bằng cách nối đoạn thẳng giữa 2 điểm với điều kiện là áp dụng công thức toán chúng mình sẽ       tính được khoảng cách nhờ toạ độ điểm của các tấm nếu khoảng cách đó bằng chiều dài, chiều rộng, chiều cao của tấm thì thực hiện việc vẽ vì sau khi xoay tấm quanh các trục       thì các kích thứơc ban đầu sẽ thay đổi nhưng mỗi tấm sau khi xoay sẽ vẫn có 3 kích thước ban đầu đó ở đầu vào ví dụ sau khi xoay chiều dài sẽ có thể biến thành chiều rộng       và có thể ngược lại. 

  * File bezierAlgo.py sử dụng thuật toán hay phương trình đường cong bezier để vẽ ra các đường cong từ việc nối rất nhiều đoạn thẳng cực nhỏ giữa các đoạn thẳng đó có độ chênh     lệch nghiêng cực nhỏ tức phương trình trên biến các điểm điều khiển đường cong thành nhiều điểm cực sát nhau có quỹ đạo trở thành đường cong rồi nối trúng lại với nhau bhằng     phương thức add_line() của ezdxf là phương thức nối đoạn thẳng giữa 2 điểm
      + Đầu tiên chúng mình lấy dữ liệu từ file svg là các tọa độ điểm của các điểm điều khiển đường cong.
      + Tiếp theo chúng mình sẽ tạo ra list d để chứa các list chứa các toạ độ điểm của từng đường cong tức mỗi list trong list d đó chứa các toạ độ điểm của 1 đường cong rồi           sau đó tạo thêm list a để chứa các list rỗng trong mỗi list rỗng đó sẽ được thêm vào các bộ toạ độ điểm mà chúng mình đã tính được là giá trị x, giá trị y nhờ áp dụng           phương trình đường cong bezier biến các điểm điều khiển đường cong thành nhiều điểm cực sát nhau có quỹ đạo trở thành đường cong.
      + Nhờ list a ở trên chúng mình sẽ thực hiện vẽ các đường cong nhờ phương thức add_line() của ezdxf là phương thức nối đoạn thẳng giữa 2 điểm.
  * Sau khi đã viết xong các đoạn mã để vẽ ở file python thì các bạn phải xuất file dxf mới thấy được bản vẽ. Trên Command Prompt gõ ```python filename.py``` rồi cài đặt phần mềm autodesk hoặc sử dụng phiên bản trên web để thấy được bản vẽ vào [liên kết](https://viewer.autodesk.com/) sau.
