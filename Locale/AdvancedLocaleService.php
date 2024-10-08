namespace App\Locale;

use Illuminate\Support\Facades\App;

class LocaleService
{
    public function switchLanguage($language)
    {
        // Switch language and update translations
        App::setLocale($language);
        session()->put('locale', $language);
    }

    public function getTranslations($language)
    {
        // Get translations for the specified language
        $translations = [];
        foreach (glob(resource_path('lang/'. $language. '/*.php')) as $file) {
            $translations = array_merge($translations, require $file);
        }

        return $translations;
    }
}
