namespace App\SocialMedia;

use Illuminate\Support\Facades\Http;

class SocialMediaService
{
    public function shareProduct($productId, $shareData)
    {
        // Share product on social media using social media APIs
        $response = Http::post('https://graph.facebook.com/v13.0/me/feed', [
            'access_token' => env('FACEBOOK_ACCESS_TOKEN'),
            'message' => $shareData['message'],
            'link' => $shareData['link'],
            'picture' => $shareData['picture']
        ]);

        return $response->json();
    }
}
