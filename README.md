 License Plate Recognition & Truck Gate Access System

Bu proje, **YOLOv5** kullanılarak eğitilmiş iki farklı nesne tespiti modeliyle **araçlardan yalnızca kamyonları** tanıyıp plakasını okuyan ve veritabanında kayıtlıysa geçiş izni veren bir güvenlik sistemidir. Proje, Python ile yazılmıştır ve **Flask** kullanılarak web arayüzü sunulmaktadır. 

Mobil cihazlar üzerinden kullanılabilir ve **ngrok** ile dış ağlardan erişim sağlanabilir.

Proje Özeti

- **YOLOv5 ile nesne tespiti**: Sadece kamyonları tanımak için özel olarak eğitilmiş bir model (`truck.pt`) kullanılır.
- **Plaka tanıma**: Tespit edilen kamyonun plakası kesilir ve OCR (optical character recognition) ile okunur.
- **Geçiş kontrolü**: Plaka, SQLite veritabanında kayıtlıysa "Kapı açılıyor", değilse "Erişim reddedildi" mesajı döner.
- **Gerçek zamanlı video akışı**: Web kamerası ile canlı görüntü alınır, model sürekli olarak analiz yapar.
- **Kullanıcı arayüzü**: Web arayüzü üzerinden plaka ekleme ve canlı video izleme mümkündür.

 Kullanılan Teknolojiler

- Python
- Flask
- OpenCV
- PyTesseract (OCR için)
- YOLOv5 (model eğitimi Colab üzerinde)
- SQLite (veritabanı)
- Ngrok (mobil ağdan erişim için)
- Roboflow (veri setleri)

## Kullanılan Datasetler

License Plate Detection Dataset : https://universe.roboflow.com/janet-rini-eaojj/license-plate-detection-tdv0k
BibTeX:
@misc{license-plate-detection-tdv0k_dataset,
  title        = { license plate detection Dataset },
  type         = { Open Source Dataset },
  author       = { Janet Rini },
  howpublished = { \url{https://universe.roboflow.com/janet-rini-eaojj/license-plate-detection-tdv0k} },
  url          = { https://universe.roboflow.com/janet-rini-eaojj/license-plate-detection-tdv0k },
  journal      = { Roboflow Universe },
  publisher    = { Roboflow },
  year         = { 2025 },
  month        = { feb },
  note         = { visited on 2025-05-25 },
}

Yolo Truck Dataset : https://universe.roboflow.com/yolo-d3ogg/yolo-truck-mfz12
BibTeX:
@misc{yolo-truck-mfz12_dataset,
  title        = { Yolo Truck Dataset },
  type         = { Open Source Dataset },
  author       = { YOLO },
  howpublished = { \url{https://universe.roboflow.com/yolo-d3ogg/yolo-truck-mfz12} },
  url          = { https://universe.roboflow.com/yolo-d3ogg/yolo-truck-mfz12 },
  journal      = { Roboflow Universe },
  publisher    = { Roboflow },
  year         = { 2022 },
  month        = { dec },
  note         = { visited on 2025-05-25 },
}


