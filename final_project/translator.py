import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class Translator():
    """
    This class provides methods to translate text from English to French and vice versa.
    """

    def __init__(self):
        authenticator = IAMAuthenticator(apikey=os.getenv("IBM_API_KEY"))
        translator = LanguageTranslatorV3(
            version="2018-05-01",
            authenticator=authenticator
        )

        translator.set_service_url(os.getenv("IBM_URL"))
        translator.set_disable_ssl_verification(True)

        self.translator = translator

    def englishToFrench(self, text):
        """
        This function translates text from English to French.
        """
        result = self.translator.translate(
            text=text, model_id="en-fr").get_result()

        return result['translations'][0]["translation"]

    def frenchToEnglish(self, text):
        """
        This function translates text from French to English.
        """

        result = self.translator.translate(
            text=text, model_id="fr-en").get_result()

        return result['translations'][0]["translation"]
