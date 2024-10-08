namespace App\Locale;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

class LocaleController extends Controller
{
    public function switchLanguage(Request $request, $language)
    {
        // Switch language and update translations
        $this->localeService->switchLanguage($language);

        return Response::redirect()->back();
    }
}
