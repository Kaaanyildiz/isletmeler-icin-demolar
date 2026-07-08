$files = @(
    "c:\Users\Msi\işletmeler için demo üretimi\betul_sel_demo.html",
    "c:\Users\Msi\işletmeler için demo üretimi\kizilcazade_demo.html",
    "c:\Users\Msi\işletmeler için demo üretimi\omer_kati_demo.html"
)

$urls = @()

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        
        $matchesSrc = [regex]::Matches($content, 'src="([^"]+)"')
        foreach ($match in $matchesSrc) {
            $url = $match.Groups[1].Value
            if ($url -match "^http") {
                $urls += [PSCustomObject]@{ File = Split-Path $file -Leaf; Url = $url }
            }
        }
        
        $matchesUrl = [regex]::Matches($content, "url\(['`""]([^'`""]+)['`""]\)")
        foreach ($match in $matchesUrl) {
            $url = $match.Groups[1].Value
            if ($url -match "^http") {
                $urls += [PSCustomObject]@{ File = Split-Path $file -Leaf; Url = $url }
            }
        }
    }
}

$urls = $urls | Sort-Object -Property Url -Unique

$results = @()

foreach ($item in $urls) {
    $url = $item.Url
    try {
        $response = Invoke-WebRequest -Uri $url -UseBasicParsing -Method Head -TimeoutSec 5 -ErrorAction Stop
        $status = $response.StatusCode
    } catch {
        try {
            $response = Invoke-WebRequest -Uri $url -UseBasicParsing -Method Get -TimeoutSec 5 -ErrorAction Stop
            $status = $response.StatusCode
        } catch {
            $status = $_.Exception.Response.StatusCode.value__
            if (-not $status) { $status = "Failed" }
        }
    }
    
    $results += [PSCustomObject]@{
        File = $item.File
        Url = $url
        Status = $status
    }
}

$results | Format-Table -AutoSize
