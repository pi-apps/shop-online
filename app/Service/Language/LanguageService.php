// LanguageService.php
namespace App\Services;

use Illuminate\Support\Facades\App;

class LanguageService {
    public function getTranslatedText($key) {
        return __($key);
    }

    public function setLocale($locale) {
        App::setLocale($locale);
    }
}
