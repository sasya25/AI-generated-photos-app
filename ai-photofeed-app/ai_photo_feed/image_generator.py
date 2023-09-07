# importing openai module
import openai

# assigning API KEY to the variable
openai.api_key = ''

class ImageGenerator:
    '''
    # TODO: remove this, used it for testing
    def generate_image(self,text):
        return "https://cdn.pixabay.com/photo/2022/09/04/05/00/halloween-7430780_1280.jpg"
    '''
    def generate_image(self, text):
        try:
            response = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024"
            )
            generated_image_url = response['data'][0]['url']
            generated_image_url = response.assets[0].url
            return generated_image_url
        except Exception as e:
            return str(e)
