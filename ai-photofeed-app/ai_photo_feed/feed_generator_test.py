
class FeedGeneratorTest:
    def __init__(self, user_id):
        self.user_id = user_id
        # Sample photos (you can replace these with your own photo URLs)
        self.photos = [
            {"id": 1, "url": "https://cdn.pixabay.com/photo/2016/10/18/21/22/beach-1751455_1280.jpg", "caption": "Beautiful beach"},
            {"id": 2, "url": "https://cdn.pixabay.com/photo/2017/02/01/22/02/mountain-landscape-2031539_1280.jpg", "caption": "Exploring the mountains"},
            {"id": 3, "url": "https://cdn.pixabay.com/photo/2015/02/24/13/23/buildings-647400_1280.jpg", "caption": "City lights at night"},
            {"id": 4, "url": "https://cdn.pixabay.com/photo/2016/03/04/22/54/animal-1236875_1280.jpg", "caption": "Panda"},
            {"id": 5, "url": "https://cdn.pixabay.com/photo/2018/05/29/10/31/dog-3438453_1280.jpg", "caption": "dog and cat"},
            {"id": 6, "url": "https://cdn.pixabay.com/photo/2017/09/12/03/57/elephant-2741176_1280.jpg", "caption": "group of elephants"},
            {"id": 7, "url": "https://cdn.pixabay.com/photo/2017/04/24/15/25/robot-2256814_1280.jpg", "caption": "aliens from moon"},
            {"id": 8, "url": "https://cdn.pixabay.com/photo/2012/03/01/00/55/flowers-19830_1280.jpg", "caption": "flowers"},
            {"id": 9, "url": "https://cdn.pixabay.com/photo/2018/05/13/07/08/sheep-3395550_1280.jpg", "caption": "sheep"},
            {"id": 10, "url": "https://cdn.pixabay.com/photo/2014/07/13/19/45/edsel-ranger-392745_1280.jpg", "caption": "yellow color taxi"},
            {"id": 11, "url": "https://cdn.pixabay.com/photo/2017/07/24/19/57/tiger-2535888_1280.jpg", "caption": "tiger"},
            {"id": 12, "url": "https://cdn.pixabay.com/photo/2015/03/01/16/52/puzzle-654957_1280.jpg", "caption": "puzzle"},
            {"id":13, "url": "https://cdn.pixabay.com/photo/2022/09/04/05/00/halloween-7430780_1280.jpg", "caption": "halloween gothic"}

        ]
    def load_images(self):
        # TODO: load images from db for this user_id
        return self.photos
    def filter_images(self, photos):
        return self.photos
    def rank_images(self, photos):
        # TODO: rank images based on  user interests
        return self.photos
    def get_feed(self,limit):
        photos = self.load_images()
        photos = self.filter_images(photos)
        photos = self.rank_images(photos)
        return photos
