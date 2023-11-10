from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.pagelayout import PageLayout


class SayHello(App):
    def build(self):
        self.window = PageLayout()
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0001.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0002.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0003.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0004.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0005.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0006.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0007.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0008.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0009.jpg"))
        self.window.add_widget(Image(source="புனித ரமளானில் புண்ணியம் பெற ஓதுங்கள் v1.0.1 - FINAL _page-0010.jpg"))

        return self.window


if __name__ == "__main__":
    SayHello().run()
