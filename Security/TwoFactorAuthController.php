namespace App\Security;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

class TwoFactorAuthController extends Controller
{
    public function authenticate(Request $request)
    {
        // Authenticate user using two-factor authentication
        $user = Auth::user();
        $token = $request->input('token');

        if ($this->twoFactorAuthService->authenticate($user, $token)) {
            return Response::redirect()->intended(route('home'));
        }

        return Response::view('security.two-factor-auth', ['error' => 'Invalid token']);
    }
}
