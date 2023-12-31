<!-- omit in toc -->
# Apache Kafka ile Basit CDC Uygulaması

## İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Container'lar](#containerlar)
- [Proje Çalışma Mantığı](#proje-çalışma-mantığı)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
  - [Docker](#docker)
  - [Kubernetes](#kubernetes)
- [LİSANS](#li̇sans)


# Proje Hakkında
Bu proje, Apache kafka ile yapılmış basit bir CDC uygulamasıdır.Projeyi çalıştırdığınızda [localhost:8000](https://localhost:8000) adresine giderek uygulamayı kullanabilirsiniz. Ayriyeten [localhost:9000](https://localhost:9000) adresine giderek kafdrop arayüzüne erişebilirsiniz. Kafdrop arayüzü ile kafka server'ı izleyebilirsiniz.


# Container'lar

Projede Toplamda 15 adet docker container bulunmaktadır. Bunlar
- 1- zookeeper (kafka için gerekli)
- 2- kafka-1 (kafka server)(Broker id: 1)
- 3- kafka-2 (kafka server)(Broker id: 2)
- 4- kafka-3 (kafka server)(Broker id: 3)
- 5- mongo (mongo db)
- 6- m1 (mongo db replica set)
- 7- m2 (mongo db replica set)
- 8- mongo-init (mongo db replica set ayarlaması için)
- 9- kafdrop (kafka arayüzü)
- 10- kafka-topics (kafka server için "X" topic oluşturmak için)
- 11- producer (kafka server'a mesaj göndermek için)
- 12- consumer1 (kafka server'dan mesaj almak için)
- 13- consumer2 (kafka server'dan mesaj almak için)
- 14- consumer3 (kafka server'dan mesaj almak için)
- 15- kafkadeneme (mongodb veritabanına kayıt eklemek için)


# Proje Çalışma Mantığı

Docker compose dosyası çalıştırıldığında uygulama ile 8000 ve 9000 portlarından iletişim kurulabilir. 8000 portu ile uygulamaya erişim sağlanabilirken 9000 portu ile kafdrop arayüzüne erişim sağlanabilir. 8000 portuna gidildiğinde karşınıza aşağıdaki gibi bir ekran gelecektir. Bu uygulama kafkadeneme container'ı üzerinden çalışmaktadır. Buradaki input bölümüne veri girilip butona basıldığında girilen veri mongodb veritabanına eklenir. Producer container'ı mongodb veritabanını ***Change Stream*** ile dinlemektedir. Change Stream ile veritabanına eklenen her kayıt kafka serverdaki X (replication factor 3) topicine gönderilir. Kafka server'dan veri alan consumer container'ları ise veriyi kafka server'dan alıp ekrana yazdırır. Aşağıdaki resimde 8000 portuna gidildiğinde karşımıza çıkan ekran görülmektedir. Buradan veri girebilir ve veritabanına kayıt ekleyebilirsiniz.
<img src="./images/img1.png" alt="Resim1">
Daha sonra kafdrop arayüzüne gidilir. Kafdrop arayüzüne gidildiğinde aşağıdaki gibi bir ekran gelecektir. Burada kafka server'ın çalıştığı görülmektedir. Ayrıca kafka server'a gönderilen mesajlar da görülmektedir.
<img src="./images/img2.png" alt="Resim2">
Docker console ekranında ise aşağıdaki gibi bir ekran görüntüsü alınır. Burada producer container'ı veritabanına kayıt eklediğinde consumer container'larına mesaj gönderdiği görülmektedir.
<img src="./images/img3.png" alt="Resim3">


# Kullanılan Teknolojiler
- [Apache Kafka](https://kafka.apache.org/)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)
- [Kafdrop](https://github.com/obsidiandynamics/kafdrop)
- [Kubernetes](https://kubernetes.io/)
- [Minikube](https://minikube.sigs.k8s.io/docs/)
- [Helm](https://helm.sh/)

# Kurulum

## Docker

Bilgisayarınızda [Docker](https://www.docker.com/) **kurulu olmalıdır**. Docker kurulumu için [Docker Desktop](https://www.docker.com/products/docker-desktop) adresini ziyaret edebilirsiniz.

1-İlk olarak projeyi klonlayın.
```sh
git clone https://github.com/TahaMuslu/.git
```

2-Daha sonra projenin bulunduğu dizine girin.
```sh
cd kafka-CDC-Project
```

3-Son olarak projeyi çalıştırın.
```sh
docker compose up
```
4-Uygulamayı çalıştırdıktan sonra `http://localhost:8000` adresine giderek veritabanına kayıt ekleyebilirsiniz. Ayrıca `http://localhost:9000` adresine giderek kafdrop arayüzüne erişebilirsiniz.Yeni kayıt eklendiğinde kafdrop arayüzünde değişiklik görülecektir ve docker console ekranında da mesajlar görülecektir.
>Portları değiştirmek için `docker-compose.yml` dosyasını düzenleyin.

5-İsteğe bağlı olarak mongodb veritabanlarına 27020(mongo), 27021(m1), 27022(m2) portlarından erişebilirsiniz. Mongodb compass ile erişebilirsiniz.

Uygulamayı Sonlandırmak İçin
```sh
docker compose down
```


## Kubernetes

İsterseniz projede bulunan ***kafka-chart*** klasörü içerisindeki chart dosyasını kullanarak kubernetes üzerinde de çalıştırabilirsiniz. Bunun için [minikube](https://minikube.sigs.k8s.io/docs/start/) ve [helm](https://helm.sh/docs/intro/install/) kurulu olmalıdır. Minikube kurulumu için [buraya](https://minikube.sigs.k8s.io/docs/start/) tıklayabilirsiniz. Helm kurulumu için [buraya](https://helm.sh/docs/intro/install/) tıklayabilirsiniz.


# LİSANS
[MIT © Taha Yasin Muslu](https://mit-license.org/)