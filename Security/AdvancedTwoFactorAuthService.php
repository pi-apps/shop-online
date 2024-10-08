namespace App\Security;

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Log;

class TwoFactorAuthService
{
    public function authenticate($user, $token)
    {
        // Authenticate user using two-factor authentication
        if ($user->two_factor_auth_enabled && $token === $user->two_factor_auth_token) {
            return true;
        }

        return false;
    }

    public function generateTwoFactorAuthToken($user)
    {
        // Generate two-factor authentication token
        $token = Str::random(6);
        $user->two_factor_auth_token = $token;
        $user->save();

        return $token;
    }
}
