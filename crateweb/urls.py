from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import jutils.ji18n.translate
jutils.ji18n.translate.patch()

from crate.web.search.views import Search


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", Search.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    #url(r"^about/", include("about.urls")),
    url(r"^account/", include("account.urls")),
    url(r"^account/", include("crate.web.social_auth.urls")),
    url(r"^admin_tools/", include("admin_tools.urls")),
    url(
        r"^social-auth/disconnect/(?P<backend>[^/]+)/(?P<association_id>[^/]+)/$",
        "crate.web.social_auth.views.disconnect",
    ),
    url(r"^social-auth/", include("social_auth.urls")),

    url(r"^users/", include("crate.web.lists.urls")),

    url(r"^packages/", include("crate.web.packages.urls")),

    url(r"^stats/", include("crate.web.packages.stats.urls")),

    url(r"^simple/", include("crate.web.packages.simple.urls")),

    #url(r"^help/", include("helpdocs.urls")),
    #url(r"^api/", include("crateweb.api_urls")),

    url(r"^", include("crate.web.search.urls")),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
